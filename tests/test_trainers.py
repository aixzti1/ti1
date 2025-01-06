import torch
from src.models.lstm_model import LSTMModel
from src.trainers.trainer_lstm import TrainerLSTM
from src.utils.config import Config

def test_trainer_lstm():
    config = Config()
    model = LSTMModel()
    x = torch.randn(50, config.seq_len, config.input_size)
    y = torch.randn(50)
    dataset = list(zip(x, y))
    loader = torch.utils.data.DataLoader(dataset, batch_size=config.batch_size)
    trainer = TrainerLSTM(model, loader, config)
    trainer.train()
    assert True
