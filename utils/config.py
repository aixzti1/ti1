class Config:
    def __init__(self):
        self.model_name = 'lstm'
        self.seq_len = 30
        self.batch_size = 16
        self.lr = 0.001
        self.epochs = 5
        self.input_size = 6
        self.hidden_size = 64
        self.num_layers = 2
