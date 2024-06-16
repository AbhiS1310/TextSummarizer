import os

from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.entity import DataValidationConfig
from textSummarizer.utils.common import create_directories


class DataValidation:
    def __init__(self,config: DataValidationConfig):
        self.config = config
        create_directories([config.root_dir])
    
    def validate(self)->bool:
        
        validation_status = False
        all_files = self.config.ALL_REQUIRED_FILES
        files = os.listdir(os.path.join("artifacts","data_ingestion","samsum_dataset"))

        for file in all_files:
            if file not in files:
                validation_status = False
                with open(self.config.STATUS_FILE, 'w') as f:
                    f.write(f"Validation status: {validation_status}")
            else:
                validation_status = True
                with open(self.config.STATUS_FILE,'w') as f:
                    f.write(f"Validation status: {validation_status}")

        return validation_status