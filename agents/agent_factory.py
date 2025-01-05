from .custom_agent import CustomAgent

class AgentFactory:
    def create_agent(self, name, config):
        return CustomAgent(name, config)
