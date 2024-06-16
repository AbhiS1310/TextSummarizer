import os
from textSummarizer.constants import *
from textSummarizer.utils.common import (read_yaml,create_directories)
from textSummarizer.entity import  DataIngestionConfig,DataValidationConfig,DataTransformationConfig

class ConfigurationManager:
    def __init__(self,config_filepath = CONFIG_FILE_PATH,params_filepath= PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_directories([self.config.root_dir])
    
    def get_data_ingestion_config(self)->DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionConfig(config.root_dir,
                                                    config.source_url,
                                                    config.local_data_file,
                                                    config.zipdir)
        return data_ingestion_config
    
    def get_data_validation_config(self)->DataValidationConfig:
        config = self.config.data_validation
        create_directories([config.root_dir])
        data_validation_config = DataValidationConfig(config.root_dir,
                                                      config.STATUS_FILE,
                                                      config.ALL_REQUIRED_FILES)
        return data_validation_config
    
    def get_data_transformation_config(self)->DataTransformationConfig:
        config = self.config.data_transformation
        create_directories([config.root_dir])
        data_transformation_config = DataTransformationConfig(config.root_dir,
                                                      config.data_path,
                                                      config.tokenizer_name)
        return data_transformation_config
