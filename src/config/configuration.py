import sys

from src.constants.paths import CONFIG_FILE_PATH
from src.entities.config_entity import DataIngestionConfig
from src.utils.common import read_yaml
from src.utils.exception import CustomException
from src.utils.logger import logging


class ConfigurationManager:

    def __init__(self):

        try:
            logging.info("Reading configuration file")

            self.config = read_yaml(CONFIG_FILE_PATH)

        except Exception as e:
            raise CustomException(e, sys)

    def get_data_ingestion_config(self) -> DataIngestionConfig:

        try:

            config = self.config["data_ingestion"]

            return DataIngestionConfig(
                train_data_file=config["train_data_file"],
                test_data_file=config["test_data_file"]
            )

        except Exception as e:
            raise CustomException(e, sys)