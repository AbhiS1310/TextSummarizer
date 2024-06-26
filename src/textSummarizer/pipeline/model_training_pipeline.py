import os

from textSummarizer.conponents.model_trainer import ModelTrainer
from textSummarizer.config.configuration import ConfigurationManager




class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(model_trainer_config)
        model_trainer.train()



