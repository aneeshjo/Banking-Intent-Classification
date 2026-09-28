import sys

from src.constants.paths import (
     CONFIG_FILE_PATH,
     PARAMS_FILE_PATH,
     SCHEMA_FILE_PATH
)
from src.entities.config_entity import(
DataIngestionConfig,
DataValidationConfig,
DataTransformationConfig
)
from src.utils.common import read_yaml
from src.utils.exception import CustomException
from src.utils.logger import logging


class ConfigurationManager:

    def __init__(self):

        try:
            logging.info("Reading configuration file")

            self.config = read_yaml(CONFIG_FILE_PATH)
            self.params = read_yaml(PARAMS_FILE_PATH)
            self.schema = read_yaml(SCHEMA_FILE_PATH)

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

    def get_data_validation_config(self) -> DataValidationConfig:

        try:

            return DataValidationConfig(
                schema_file=str(SCHEMA_FILE_PATH)
            )

        except Exception as e:

            raise CustomException(e, sys)

    def get_data_transformation_config(
        self
    ) -> DataTransformationConfig:

        try:

            config = self.params["data_transformation"]

            return DataTransformationConfig(
                text_column=config["text_column"],
                target_column=config["target_column"],
                lowercase=config["lowercase"],
                remove_extra_whitespace=config["remove_extra_whitespace"]
            )

        except Exception as e:

            raise CustomException(e, sys)