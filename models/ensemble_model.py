import torch
import torch.nn as nn
from .lstm_model import LSTMModel
from .transformer_model import TransformerModel

class EnsembleModel(nn.Module):
    def __init__(self, input_size=6, hidden_size=64):
        super().__init__()
        self.lstm_model = LSTMModel(input_size, hidden_size)
        self.transformer_model = TransformerModel(input_size, hidden_size, 4, 2)
        self.fc = nn.Linear(2, 1)
    def forward(self, x):
        out_lstm = self.lstm_model(x)
        out_transformer = self.transformer_model(x)
        combined = torch.cat([out_lstm, out_transformer], dim=1)
        out = self.fc(combined)
        return out
