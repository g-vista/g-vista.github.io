import torch

class ContextAgent:
    def __init__(self, config=None):
        self.config = config or {}
    
    def analyze(self, video, prompt):
        return "Scene matches prompt well, cat behavior is realistic."
