import pandas as pd
import numpy as np

def run_backtest(df, signals):
    balance = 1000
    position = 0
    for i in range(len(signals)):
        if signals[i] == 'BUY' and position == 0:
            position = balance / df['close'].iloc[i]
            balance = 0
        elif signals[i] == 'SELL' and position > 0:
            balance = position * df['close'].iloc[i]
            position = 0
    if position > 0:
        balance = position * df['close'].iloc[-1]
        position = 0
    return balance
