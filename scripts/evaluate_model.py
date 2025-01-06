import torch
from sklearn.metrics import mean_squared_error

def evaluate(model, loader):
    model.eval()
    preds = []
    trues = []
    with torch.no_grad():
        for i, x, y in enumerate(loader):
            out = model(x)
            preds.extend(out.squeeze().tolist())
            trues.extend(y.tolist())
    mse = mean_squared_error(trues, preds)
    return mse
