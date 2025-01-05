import pandas as pd
import numpy as np

class FeatureEngineering:
    def __init__(self, df):
        self.df = df
    def create_features(self):
        self.df['return'] = self.df['close'].pct_change()
        self.df['ma_10'] = self.df['close'].rolling(window=10).mean().fillna(method='bfill')
        self.df['ma_30'] = self.df['close'].rolling(window=30).mean().fillna(method='bfill')
        self.df['volatility'] = self.df['return'].rolling(window=10).std().fillna(method='bfill')
        self.df = self.df.dropna()
        return self.df
