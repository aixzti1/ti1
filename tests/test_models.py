import torch
from src.models.lstm_model import LSTMModel
from src.models.transformer_model import TransformerModel
from src.models.ensemble_model import EnsembleModel

def test_lstm_shape():
    model = LSTMModel()
    x = torch.randn(2, 30, 6)
    y = model(x)
    assert len(y.shape) == 2

def test_transformer_shape():
    model = TransformerModel()
    x = torch.randn(2, 30, 6)
    y = model(x)
    assert len(y.shape) == 2

def test_ensemble_shape():
    model = EnsembleModel()
    x = torch.randn(2, 30, 6)
    y = model(x)
    assert len(y.shape) == 2
