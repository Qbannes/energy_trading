import numpy as np
import torch.nn as nn
import torch
from .load_scalers import build_features, seq_len, num_features

def preprocess_Binance_data(opens, highs, lows, closes, volumes, train_scalers):
    # Build features
    features, num_features, train_scalers = build_features(opens, highs, lows, closes, volumes, train_scalers)

    x = np.expand_dims(features, axis=0)

    # Scale features
    for i in range(num_features):
        x_scaled = train_scalers[i].transform(x[:, :, i].reshape(-1, 1)) # DO NOT use "fit_transform"
        x[:, :, i] = x_scaled.reshape(x.shape[0], x.shape[1])

    return x




class Model(nn.Module):
    ...
    
MODELS_INFOS = [
    {
    "paths": [
        "trading_bot/ensemble_models/YOUR_MODEL_NAME.pt",
    ],"architecture": Model,
    },
]



MODELS = []

def load_model():
    for index, model_info in enumerate(MODELS_INFOS):
        print(f"Loading model {index+1} ...")

        model_paths = model_info["paths"]
        architecture = model_info["architecture"]

        for model_path in model_paths:
            # Initialize model
            model = architecture()

            # Load trained weights
            model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
            model.to('cpu')

            # Add model to the list
            MODELS.append(model)


def get_action(opens, highs, lows, closes, volumes, train_scalers):
    combined_actions = []

    # Preprocess new data
    scaled_x = preprocess_Binance_data(opens, highs, lows, closes, volumes, train_scalers) # shape: (1, seq_len, n_features)
    scaled_x = torch.from_numpy(scaled_x.astype(np.float32))

    with torch.no_grad():
        for model in MODELS:
            model.train(False)

            y_pred = model(scaled_x).detach().cpu().numpy()

            action = y_pred[0, 0] > 0 # 0: Sell, 1: Buy
            combined_actions.append(action)

    final_action = 1 if combined_actions.count(1) > combined_actions.count(0) else 0
    return final_action




