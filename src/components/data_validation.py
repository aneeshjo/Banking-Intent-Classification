import sys

import pandas as pd

from src.entities.config_entity import DataValidationConfig
from src.utils.common import read_yaml
from src.utils.exception import CustomException
from src.utils.logger import logging


class DataValidation:

    def __init__(self, config: DataValidationConfig):

        self.config = config
        self.schema = read_yaml(self.config.schema_file)

    def validate_columns(self, dataframe: pd.DataFrame) -> bool:

        try:

            logging.info("Starting column validation")

            required_columns = self.schema["data_validation"]["required_columns"]

            actual_columns = list(dataframe.columns)

            missing_columns = [
                column
                for column in required_columns
                if column not in actual_columns
            ]

            if missing_columns:

                logging.error(
                    f"Missing columns: {missing_columns}"
                )

                return False

            logging.info("Column validation successful")

            return True

        except Exception as e:

            logging.error("Column validation failed")

            raise CustomException(e, sys)

    def validate_missing_values(self, dataframe: pd.DataFrame) -> bool:

        try:

            logging.info("Starting missing-value validation")

            required_columns = self.schema["data_validation"]["required_columns"]

            missing_values = dataframe[required_columns].isnull().sum()

            total_missing_values = missing_values.sum()

            if total_missing_values > 0:

                logging.error(
                    f"Missing values found:\n{missing_values}"
                )

                return False

            logging.info("Missing-value validation successful")

            return True

        except Exception as e:

            logging.error("Missing-value validation failed")

            raise CustomException(e, sys)

    def validate_num_classes(self, dataframe: pd.DataFrame) -> bool:

        try:

            logging.info("Starting class-count validation")

            target_column = self.schema["data_validation"]["target_column"]

            expected_num_classes = self.schema[
                "data_validation"
            ]["expected_num_classes"]

            actual_num_classes = dataframe[target_column].nunique()

            if actual_num_classes != expected_num_classes:

                logging.error(
                    f"Expected {expected_num_classes} classes, "
                    f"but found {actual_num_classes}"
                )

                return False

            logging.info(
                f"Class-count validation successful: "
                f"{actual_num_classes} classes"
            )

            return True

        except Exception as e:

            logging.error("Class-count validation failed")

            raise CustomException(e, sys)

    def validate(self, train_data: pd.DataFrame, test_data: pd.DataFrame) -> bool:

        try:

            logging.info("Starting data validation")

            train_valid = (
                self.validate_columns(train_data)
                and self.validate_missing_values(train_data)
                and self.validate_num_classes(train_data)
            )

            test_valid = (
                self.validate_columns(test_data)
                and self.validate_missing_values(test_data)
                and self.validate_num_classes(test_data)
            )

            validation_status = train_valid and test_valid

            if validation_status:

                logging.info("Data validation completed successfully")

            else:

                logging.error("Data validation failed")

            return validation_status

        except Exception as e:

            logging.error("Data validation failed")

            raise CustomException(e, sys)