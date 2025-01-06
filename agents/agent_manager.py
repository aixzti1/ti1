import os
import pickle

class AgentManager:
    def __init__(self, save_path='agents/'):
        self.save_path = save_path

    def delete_agent(self, name):
        path = os.path.join(self.save_path, f'{name}.pkl')
        if os.path.exists(path):
            os.remove(path)
    def list_agents(self):
        if not os.path.exists(self.save_path):
            return []
        return [f.split('.pkl')[0] for f in os.listdir(self.save_path) if f.endswith('.pkl')]
    def save_agent(self, agent):
        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path)
        with open(os.path.join(self.save_path, f'{agent.name}.pkl'), 'wb') as f:
            pickle.dump(agent, f)
    def load_agent(self, name):
        with open(os.path.join(self.save_path, f'{name}.pkl'), 'rb') as f:
            return pickle.load(f)
