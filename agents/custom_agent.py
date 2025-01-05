class CustomAgent:
    def __init__(self, name, config):
        self.name = name
        self.config = config
    def update_config(self, new_config):
        for k, v in new_config.items():
            setattr(self.config, k, v)
    def get_config(self):
        return self.config
