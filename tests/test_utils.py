import torch
from src.utils.signal_generator import generate_signal

def test_signal():
    s1 = generate_signal(100, 101)
    s2 = generate_signal(100, 99)
    s3 = generate_signal(100, 100)
    assert s1 == 'BUY'
    assert s2 == 'SELL'
    assert s3 == 'HOLD'
