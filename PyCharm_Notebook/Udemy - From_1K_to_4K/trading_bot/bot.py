import asyncio
import logging
import pickle
import time
import ccxt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

import ccxt.async_support as ccxt_supp
from binance.client import Client
from binance.client import AsyncClient

def setup_logger(name, log_file, level=logging.INFO):
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    handler = logging.FileHandler(log_file)        
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger

class Bot:
    def __init__(self, seq_len):
        self.logger = setup_logger('log', 'log.log')

        self.seq_len = seq_len
        self.TIME_FRAME = '15m'
        self.pos_size = 0.001 # minimum: 0.001 BTC
        self.leverage = 90
        self.slippage_percentage = 0.05 # 

        self.coin = 'BTC'
        self.price_notional = 0 
        self.size_notional = 3 # 0.1234 BTC -> 0.123 BTC
        self.asset_usd = 'USDC'
        self.model_symbol = f'{self.coin}USDT' # The pair model was trained on
        self.symbol = f"{self.coin}/{self.asset_usd}" # The pair we actually trade with
        self.symbol_ = self.symbol.replace("/", "") # The pair we actually trade with

        self.position = "NONE" # Current position Long/Short
        self.open_prices = []
        self.actions = []
        self.equities = [] 
        self.total_fee = 0 
        self.last_sec_wait = 1


    def write_to_log(self, msg):
        self.logger.info(msg)
        print(msg)



    async def create_exchange(self):
        apiKey = "YOUR_API_KEY"
        secret = "YOUR_SCRET_KEY"

        for _ in range(20):
            try:
                self.client_fut = await AsyncClient.create(api_key=apiKey, 
                                                           api_secret=secret)

                self.exchange_supp = ccxt_supp.binance({'apiKey': apiKey, 
                                                        'secret': secret,
                                                        'options': {'adjustForTimeDifference': True,  # Enable automatic time adjustment
                                                        },})
                await self.exchange_supp.load_time_difference()  # Async time sync

                self.client = ccxt.binance()
                self.write_to_log(f"Exchange created.")
                break
            except Exception as err:
                time.sleep(0.4)
                self.write_to_log(f"Failed to get account with API key {str(err)}")

        for _ in range(20):
            try:
                self.client_fut.FUTURES_URL = 'https://fapi.binance.com/fapi' 
                await self.client_fut.futures_change_leverage(symbol=self.symbol_, leverage=self.leverage)
                break
            except Exception as e:
                self.write_to_log(f"Failed to change leverage: {e}")


    async def get_candles(self, symbol):
        klines = self.client.fetch_ohlcv(symbol, self.TIME_FRAME, limit=self.seq_len+1)
        klines = np.array(klines, dtype=object) # Convert to NumPy array

        # Extract columns
        open_times = pd.to_datetime(klines[:, 0].astype(np.int64), unit='ms')
        open_prices = klines[:, 1].astype(float)
        high_prices = klines[:, 2].astype(float)
        low_prices = klines[:, 3].astype(float)
        close_prices = klines[:, 4].astype(float)
        volumes = klines[:, 5].astype(float)

        return open_times, open_prices, high_prices, low_prices, close_prices, volumes


    async def update_new_data_for_model(self):
        """
        This async function fetches the latest OHLCV data every 15 minutes, 
        extracts completed candle values (Open, High, Low, Close, Volume), 
        and stores them as NumPy arrays. 
        Later used as input for the model’s predictions.
        """
        self.write_to_log("... Getting the new candle ...")
        while True: # Start loop check new candle
            try:
                try:
                    # Fetch candles 'BTC/USDT' because the model learned on this pair
                    open_times, opens, highs, lows, closes, volumes = await self.get_candles(self.model_symbol)
                    self.opens_USDT   = np.array(opens[:-1], dtype=np.float32)  # open (exclude current candle)
                    self.highs_USDT   = np.array(highs[:-1], dtype=np.float32)  # high (exclude current candle)
                    self.lows_USDT    = np.array(lows[:-1], dtype=np.float32)   # low (exclude current candle)
                    self.closes_USDT  = np.array(closes[:-1], dtype=np.float32) # close (exclude current candle)
                    self.volumes_USDT = np.array(volumes[:-1], dtype=np.float32) # volume (exclude current candle)
                    break
                except Exception as err: 
                    await asyncio.sleep(0.2)
                    self.write_to_log(f"Failed to fetch_ohlcv('{self.coin}/USDT') {str(err)}")

            except Exception as err: 
                self.write_to_log(f"Error in update_new_data_for_model: {str(err)}")
                await asyncio.sleep(0.4)



    async def update_curr_futures_prices(self):
        for _ in range(25):
            try:
                # Fetch the latest 15-minute candle
                klines = await self.client_fut.futures_klines(
                    symbol=self.symbol_,
                    interval=Client.KLINE_INTERVAL_15MINUTE,
                    limit=1,
                )
                klines = np.array(klines, dtype=np.float32)
                self.curr_open = klines[-1, 1] # Update current open price
                self.curr_close = klines[-1, 4] # Update current close price
                self.write_to_log(f'curr close: {self.curr_close}')
                break

            except Exception as err: 
                self.write_to_log(f"Error in update_curr_futures_prices: {str(err)}")



    async def place_limit_buy_order(self, is_double_size=False, size=None):
        slippage_price = np.round(self.curr_close * self.slippage_percentage / 100, 5) 
        order_price = self.curr_close - slippage_price 
        order_price = np.round(order_price, self.price_notional) 

        if size == None:
            if is_double_size:
                size = np.round(self.pos_size * 2, self.size_notional)
            else:
                size = self.pos_size

        for _ in range(10):
            try:
                order = await self.client_fut.futures_create_order(
                    symbol=self.symbol_,
                    side='BUY',
                    type='LIMIT',
                    quantity=size, 
                    timeInForce='GTC',
                    price = order_price,
                )
                order_id = order['orderId']
                self.write_to_log(f"Buy Order placed - Price: {order_price}, Quantity: {self.pos_size}")
                self.write_to_log(f"Order details: {order}")
                break

            except Exception as e:
                await asyncio.sleep(0.4)
                self.write_to_log(f"FAILED to placed Future limit BUY: {str(e)}")

        return order_id







    async def place_limit_sell_order(self, is_double_size=False, size=None):

        slippage_price = np.round(self.curr_close * self.slippage_percentage / 100, 5) 
        order_price = self.curr_close + slippage_price 
        order_price = np.round(order_price, self.price_notional) 

        if size==None:
            if is_double_size:
                size = np.round(self.pos_size * 2, self.size_notional)
            else:
                size = self.pos_size

        for _ in range(10):
            try:
                order = await self.client_fut.futures_create_order(
                    symbol=self.symbol_,
                    side='SELL',
                    type='LIMIT',
                    quantity=size, 
                    timeInForce='GTC',
                    price = order_price,
                )
                order_id = order['orderId']
                self.write_to_log(f"Sell Order placed - Price: {order_price}, Quantity: {self.pos_size}")
                break

            except Exception as e:
                self.write_to_log(f"FAILED to placed Future limit SELL: {str(e)}")
                await asyncio.sleep(0.4)

        return order_id







    async def check_positions(self):
        for _ in range(20):
            try:
                positions = await self.client_fut.futures_position_information()
                break
            except Exception as e:
                self.write_to_log(f"Err check_positions: {e}")
                await asyncio.sleep(0.2)

        active_positions = [p for p in positions if float(p['positionAmt']) != 0]
        
        if not active_positions:
            self.position = "NONE"
            position_size = 0
            self.write_to_log("No open positions found...")
        else:
            self.write_to_log(f"Found {len(active_positions)} open positions:")
            for pos in active_positions:
                if pos['symbol'] == self.symbol_:
                    position_size = np.round(float(pos['positionAmt']), 4)

                    if 0 < np.abs(position_size) < self.pos_size:
                        self.write_to_log(f"WARNING: Position size is too small: {position_size} {self.coin}")

                    if position_size > 0:
                        self.position = "LONG" # buy
                    elif position_size < 0:
                        self.position = "SHORT" # sell

                    self.write_to_log(f"Current position: {self.position}. Position size: {position_size} {self.coin} ")



    async def check_equity(self):
        for _ in range(10):
            try:
                futures_balance = await self.client_fut.futures_account_balance()
                
                # Filter for USDC
                usdc_balance = next((item for item in futures_balance if item['asset'] == self.asset_usd), None) 
                self.equity = float(usdc_balance['balance']) if usdc_balance else 0.0
                self.write_to_log(f"Equity: {self.equity:.2f}")
                break
            
            except Exception as e:
                self.write_to_log(f"Error check_equity: {e}")

        self.equity = np.round(self.equity, 2)



    async def cancel_order(self):
        for _ in range(2):
            try:
                result = await self.client_fut.futures_cancel_all_open_orders(symbol=self.symbol_)
                
                self.write_to_log(f"Canceled order: {result}")

            except Exception as err:
                self.write_to_log(f"Couldn't cancel orders: {err}")
                await asyncio.sleep(0.3)


    async def get_order_fee(self, order_id):
        if order_id:
            for _ in range(10):
                try:
                    # Fetch trades related to this symbol
                    trades = await self.client_fut.futures_account_trades(symbol=self.symbol_)

                    # Filter for trades that belong to this order_id
                    order_trades = [t for t in trades if int(t['orderId']) == int(order_id)]

                    if not order_trades:
                        self.write_to_log(f"No trades found for order_id {order_id}")
                        return 0.0

                    # Sum up the commission from all fills
                    total_fee = sum(float(t['commission']) for t in order_trades)
                    commission_asset = order_trades[0]['commissionAsset']  # e.g., USDT or USDC

                    self.write_to_log(f"Order {order_id} fee: {total_fee} {commission_asset}")
                    return total_fee

                except Exception as e:
                    self.write_to_log(f"Error get_order_fee {order_id}: {e}")
                    await asyncio.sleep(0.2)

        return 0.0


    def save(self):
        self.saved_data = {
            "open_prices": self.open_prices,
            'actions': self.actions,
            'equities': self.equities,
            'total_fee': self.total_fee,
        }
        with open("./trading_bot/saved_data.pkl", "wb") as file:
            pickle.dump(self.saved_data, file)


    def load(self):
        try:
            with open("./trading_bot/saved_data.pkl", "rb") as file:
                self.saved_data = pickle.load(file)

            self.open_prices = self.saved_data["open_prices"]
            self.actions = self.saved_data['actions']
            self.equities = self.saved_data['equities']
            self.total_fee = self.saved_data['total_fee']
        except:
            print(f"No saved_data to load!")


    async def close(self):
        for _ in range(20):
            try:
                await self.exchange_supp.close()
                await asyncio.sleep(0.1)
                await self.client_fut.close_connection()
                await asyncio.sleep(0.1)
                break
            except Exception as err:
                await asyncio.sleep(0.5)
                print(f"Failed to close connection. Err: " + str(err))



    def plot_performance(self):
        try:
            scaler = MinMaxScaler(feature_range=(min(self.equities), max(self.equities)))
            scaled_open_prices = scaler.fit_transform(np.array(self.open_prices).reshape(-1, 1)).flatten() 

            chart_title = f"Equity: ${self.equity:.2f}"
            plt.figure(figsize=(12, 6))
            plt.plot(scaled_open_prices, color='green', label='BTC Price')
            plt.plot(self.equities, label="Equity Curve", color="blue")
            plt.title(chart_title)
            plt.xlabel("Time Step")
            plt.ylabel("Equity (USD)")
            plt.legend()
            plt.grid(True)
            plt.savefig('./trading_bot/performance.png', dpi=300)
            plt.close()

        except Exception as e:
            print(f"Couldn't plot the graph: {e}")



















