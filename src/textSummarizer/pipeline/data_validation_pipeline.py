import os

from textSummarizer.conponents.data_validation import DataValidation
from textSummarizer.config.configuration import ConfigurationManager


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        validation_config = config.get_data_validation_config()
        data_validation = DataValidation(validation_config)
        data_validation.validate()