import torch

class CryptoDataset(torch.utils.data.Dataset):
    def __init__(self, data, seq_len=40):
        self.data = data
        self.seq_len = seq_len
    def __len__(self):
        return len(self.data) - self.seq_len
    def __getitem__(self, idx):
        x = self.data.iloc[idx:idx+self.seq_len].values
        y = self.data['close'].iloc[idx+self.seq_len]
        return torch.tensor(x, dtype=torch.float), torch.tensor(y, dtype=torch.float)
