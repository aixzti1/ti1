import torch

def train_model(model, loader, criterion, optimizer, epochs):
    for _ in range(epochs):
        for x, y in loader:
            optimizer.zero_grad()
            preds = model(x)
            loss = criterion(preds, y.unsqueeze(1))
            loss.backward()
            optimizer.step()
