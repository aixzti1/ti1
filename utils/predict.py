import torch

def predict_signal(model, x):
    model.eval()
    with torch.no_grad():
        y = model(x)
    return y.item()
