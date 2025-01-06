import torch
import os
import pandas as pd
import numpy as np
import ccxt
from data.crypto_dataset import CryptoDataset
from data.data_preprocessor import DataPreprocessor
from data.feature_engineering import FeatureEngineering
from models.lstm_model import LSTMModel
from models.transformer_model import TransformerModel
from models.ensemble_model import EnsembleModel
from trainers.trainer_lstm import TrainerLSTM
from trainers.trainer_transformer import TrainerTransformer
from trainers.trainer_ensemble import TrainerEnsemble
from utils.predict import predict_signal
from utils.signal_generator import generate_signal
from utils.twitter_client import tweet_signal
from utils.config import Config
from utils.logger import Logger
from agents.agent_factory import AgentFactory
from agents.agent_manager import AgentManager


def get_crypto_data(symbol='BTC/USDT', limit=500):
    exchange = ccxt.binance()
    data = exchange.fetch_ohlcv(symbol, timeframe='1h', limit=limit)
    df = pd.DataFrame(data, columns=['time','open','high','low','close','volume'])
    df.set_index('time', inplace=True)
    return df


def select_model(model_name, input_size, hidden_size, num_layers):
    if model_name == 'lstm':
        return LSTMModel(input_size=input_size, hidden_size=hidden_size, num_layers=num_layers)
    elif model_name == 'transformer':
        return TransformerModel(input_size=input_size, d_model=hidden_size, nhead=4, num_layers=num_layers)
    else:
        return EnsembleModel(input_size=input_size, hidden_size=hidden_size)


def main():
    config = Config()
    logger = Logger()
    agent_manager = AgentManager()
    factory = AgentFactory()
    user_agent = factory.create_agent('my_custom_agent', config)
    user_agent.update_config({'model_name': 'transformer'})
    agent_manager.save_agent(user_agent)
    df = get_crypto_data()
    processor = DataPreprocessor(df)
    processed_data = processor.process()
    features = FeatureEngineering(processed_data).create_features()
    dataset = CryptoDataset(features, seq_len=user_agent.get_config().seq_len)
    loader = torch.utils.data.DataLoader(dataset, batch_size=user_agent.get_config().batch_size, shuffle=True)
    model = select_model(user_agent.get_config().model_name, user_agent.get_config().input_size, user_agent.get_config().hidden_size, user_agent.get_config().num_layers)
    if user_agent.get_config().model_name == 'lstm':
        trainer = TrainerLSTM(model, loader, user_agent.get_config())
    elif user_agent.get_config().model_name == 'transformer':
        trainer = TrainerTransformer(model, loader, user_agent.get_config())
    else:
        trainer = TrainerEnsemble(model, loader, user_agent.get_config())
    trainer.train()
    last_seq = torch.tensor(features[-user_agent.get_config().seq_len:].values, dtype=torch.float).unsqueeze(0)
    pred = predict_signal(model, last_seq)
    last_price = features['close'].iloc[-1]
    signal = generate_signal(last_price, pred)
    api_key = os.getenv('TWITTER_API_KEY')
    api_key_secret = os.getenv('TWITTER_API_KEY_SECRET')
    access_token = os.getenv('TWITTER_ACCESS_TOKEN')
    access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
    tweet_signal(api_key, api_key_secret, access_token, access_token_secret, f'Signal: {signal}')
    logger.log(f'Signal: {signal}')


if __name__ == '__main__':
    main()
