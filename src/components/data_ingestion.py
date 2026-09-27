import sys
import pandas as pd

from src.entities.config_entity import DataIngestionConfig
from src.utils.exception import CustomException
from src.utils.logger import logging

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config

    def load_data(self):
        try:
            logging.info("Data Ingestion Started")

            train_data=pd.read_csv(self.config.train_data_file)

            test_data=pd.read_csv(self.config.test_data_file)

            logging.info(
                f"Training data loaded successfully: {train_data.shape}"
            )

            logging.info(
                f"Test data loaded successfully: {test_data.shape}"
            )

            return train_data, test_data

        except Exception as e:

            logging.error("Data ingestion failed")

            raise CustomException(e, sys)