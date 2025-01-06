import torch
import torch.nn as nn

class TransformerModel(nn.Module):
    def __init__(self, input_size=8, d_model=128, nhead=4, num_layers=2):
        super().__init__()
        self.linear_in = nn.Linear(input_size, d_model)
        encoder_layer = nn.TransformerEncoderLayer(d_model=d_model, nhead=nhead)
        self.transformer_encoder = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)
        self.fc_out = nn.Linear(d_model, 1)
    def forward(self, x):
        x = self.linear_in(x)
        x = x.permute(1, 0, 2)
        x = self.transformer_encoder(x)
        x = x[-1]
        x = self.fc_out(x)
        return x
