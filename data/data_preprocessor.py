import pandas as pd

class DataPreprocessor:
    def __init__(self, df):
        self.df = df
    def process(self):
        self.df = self.df.dropna()
        self.df = self.df[self.df['close'] > 0]
        self.df = self.df.sort_index()
        return self.df
