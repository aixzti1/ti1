import torch
import torch.nn as nn
import torch.optim as optim

class TrainerEnsemble:
    def __init__(self, model, loader, config):
        self.model = model
        self.loader = loader
        self.config = config
        self.criterion = nn.MSELoss()
        self.optimizer = optim.Adam(self.model.parameters(), lr=config.lr)
    def train(self):
        for _ in range(self.config.epochs):
            for x, y in self.loader:
                self.optimizer.zero_grad()
                preds = self.model(x)
                loss = self.criterion(preds, y.unsqueeze(1))
                loss.backward()
                self.optimizer.step()
