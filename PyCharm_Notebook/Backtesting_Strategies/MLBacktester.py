
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier # added (from sklearn v. 1.7)
import matplotlib.pyplot as plt
plt.style.use("seaborn-v0_8")

class MLBacktester():
    ''' Klasse für vektorisierte Backtesting von ML-Trading-Strategien (Klassifikation).
        Vorhersage: sign(next_return) ∈ {+1, 0, -1} basierend auf lagged returns.
    '''
    def __init__(self, symbol, start, end, tc):
        ''' Konstruktor: Initialisiert Backtester mit Symbol, Zeitraum, Kosten.

        Parameters
        ----------
        symbol: str          - Ticker (z.B. "EURUSD" aus CSV)
        start: str           - Start-Datum ('YYYY-MM-DD')
        end: str             - End-Datum ('YYYY-MM-DD')
        tc: float            - Transaktionskosten pro Trade (z.B. 0.00007 = 0.007%)
        '''
        self.symbol = symbol
        self.start = start
        self.end = end
        self.tc = tc
        self.model = OneVsRestClassifier(LogisticRegression(C = 1e6, max_iter = 100000)) # new (from sklearn v. 1.7)
        self.results = None
        self.get_data()
    
    def __repr__(self):
        ''' String-Repräsentation für print(mlbt) - zeigt Parameter übersichtlich.
        '''
        rep = "MLBacktester(symbol = {}, start = {}, end = {}, tc = {})"
        return rep.format(self.symbol, self.start, self.end, self.tc)
                             
    def get_data(self):
        ''' Lädt OHLC-Daten aus CSV, bereitet price/returns vor.

        Schritte:
        1. Lese "five_minute_pairs.csv" (5-Min-FX-Daten: EURUSD, GBPUSD, EURAUD)
        2. Filtere auf self.symbol (z.B. nur EURUSD-Spalte)
        3. Schneide Zeitraum [start:end]
        4. Umbenenne in "price"
        5. Berechne log-returns: returns_t = log(price_t / price_{t-1})
        '''
        raw = pd.read_csv("five_minute_pairs.csv", parse_dates = ["time"], index_col = "time")
        raw = raw[self.symbol].to_frame().dropna()
        raw = raw.loc[self.start:self.end]
        raw.rename(columns={self.symbol: "price"}, inplace=True)
        raw["returns"] = np.log(raw / raw.shift(1))
        self.data = raw
                             
    def split_data(self, start, end):
        ''' Einfacher Datenschnitt: Kopie von self.data[ start:end ].

        Warum copy()? Verhindert "SettingWithCopyWarning" bei späteren Änderungen.
        '''
        data = self.data.loc[start:end].copy()
        return data
    
    def prepare_features(self, start, end):
        ''' Erstellt Lagged-Features für ML (autoregressive Vorhersage).

        Features: lag1=returns_{t-1}, lag2=returns_{t-2}, ..., lagN=returns_{t-N}
        Target:  sign(returns_t) ∈ {+1, 0, -1}
        '''
        self.data_subset = self.split_data(start, end)
        self.feature_columns = []
        for lag in range(1, self.lags + 1):
            col = "lag{}".format(lag)
            self.data_subset[col] = self.data_subset["returns"].shift(lag)
            self.feature_columns.append(col)
        self.data_subset.dropna(inplace=True)

    def scale_features(self, recalc = True): # Newly added
        ''' Standardisiert Features: z = (x - μ_train) / σ_train

        recalc=True:  Berechne μ/σ aus aktuellem data_subset (TRAINING)
        recalc=False: Nutze gespeicherte μ/σ (TESTING → gleiche Skalierung!)
        '''
        if recalc:
            self.means = self.data_subset[self.feature_columns].mean()
            self.stand_devs = self.data_subset[self.feature_columns].std()
        
        self.data_subset[self.feature_columns] = (self.data_subset[self.feature_columns] - self.means) / self.stand_devs
        
    def fit_model(self, start, end):
        ''' Komplettes Training: Features → Scale → Fit.

        Target: np.sign(returns) = +1 (up), 0 (flat), -1 (down)
        '''
        self.prepare_features(start, end)
        self.scale_features(recalc = True) # calculate mean & std of train set and scale train set
        self.model.fit(self.data_subset[self.feature_columns], np.sign(self.data_subset["returns"]))
        
    def test_strategy(self, train_ratio = 0.7, lags = 5):
        ''' HAUPTMETHODE: Komplettes Backtesting.

        Workflow:
        1. Split: train_ratio → train_end, rest → test
        2. Train: fit_model(train_start, train_end)
        3. Test:  prepare_features(test_start, test_end)
        4. Scale test mit TRAIN-μ/σ
        5. Predict → strategy_returns = pred * returns
        6. Costs: trades = |pred.diff()|
        7. Cumulative: exp(cumsum())
        '''
        self.lags = lags
                  
        # determining datetime for start, end and split (for training an testing period)
        full_data = self.data.copy()
        split_index = int(len(full_data) * train_ratio)
        split_date = full_data.index[split_index-1]
        train_start = full_data.index[0]
        test_end = full_data.index[-1]
        
        # fit the model on the training set
        self.fit_model(train_start, split_date)
        
        # prepare the test set
        self.prepare_features(split_date, test_end)
        self.scale_features(recalc = False) # Newly added -> scale test set features with train set mean & std
                  
        # make predictions on the test set
        predict = self.model.predict(self.data_subset[self.feature_columns])
        self.data_subset["pred"] = predict
        
        # calculate Strategy Returns
        self.data_subset["strategy"] = self.data_subset["pred"] * self.data_subset["returns"]
        
        # determine the number of trades in each bar
        self.data_subset["trades"] = self.data_subset["pred"].diff().fillna(0).abs()
        
        # subtract transaction/trading costs from pre-cost return
        self.data_subset.strategy = self.data_subset.strategy - self.data_subset.trades * self.tc
        
        # calculate cumulative returns for strategy & buy and hold
        self.data_subset["creturns"] = self.data_subset["returns"].cumsum().apply(np.exp)
        self.data_subset["cstrategy"] = self.data_subset['strategy'].cumsum().apply(np.exp)
        self.results = self.data_subset
        
        perf = self.results["cstrategy"].iloc[-1] # absolute performance of the strategy
        outperf = perf - self.results["creturns"].iloc[-1] # out-/underperformance of strategy
        
        return round(perf, 6), round(outperf, 6)
        
    def plot_results(self):
        ''' Plots the performance of the trading strategy and compares to "buy and hold".
        '''
        if self.results is None:
            print("Run test_strategy() first.")
        else:
            title = "Logistic Regression: {} | TC = {}".format(self.symbol, self.tc)
            self.results[["creturns", "cstrategy"]].plot(title=title, figsize=(12, 8))
