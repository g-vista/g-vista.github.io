import torch

class ReasoningAgent:
    def __init__(self, config=None):
        self.config = config or {}
    
    def refine_prompt(self, prompt, feedback, video):
        return f"{prompt}, with warm jazz club lighting and enhanced piano audio"
