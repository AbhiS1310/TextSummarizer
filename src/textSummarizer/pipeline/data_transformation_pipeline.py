import os

from textSummarizer.conponents.data_transformation import DataTransformation
from textSummarizer.config.configuration import ConfigurationManager


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(transformation_config)
        data_transformation.convert()