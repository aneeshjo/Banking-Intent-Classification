import re
import sys

import pandas as pd

from src.entities.config_entity import DataTransformationConfig
from src.utils.exception import CustomException
from src.utils.logger import logging


class DataTransformation:

    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def transform_text(self, text: str) -> str:

        try:

            if self.config.lowercase:
                text = text.lower()

            if self.config.remove_extra_whitespace:
                text = re.sub(r"\s+", " ", text).strip()

            return text

        except Exception as e:

            raise CustomException(e, sys)

    def transform_dataframe(
        self,
        dataframe: pd.DataFrame
    ) -> pd.DataFrame:

        try:

            logging.info("Starting text transformation")

            transformed_dataframe = dataframe.copy()

            text_column = self.config.text_column

            transformed_dataframe[text_column] = (
                transformed_dataframe[text_column]
                .astype(str)
                .apply(self.transform_text)
            )

            logging.info("Text transformation completed")

            return transformed_dataframe

        except Exception as e:

            logging.error("Text transformation failed")

            raise CustomException(e, sys)

    def transform(
        self,
        train_data: pd.DataFrame,
        test_data: pd.DataFrame
    ):

        try:

            logging.info("Starting data transformation")

            transformed_train_data = self.transform_dataframe(
                train_data
            )

            transformed_test_data = self.transform_dataframe(
                test_data
            )

            logging.info("Data transformation completed successfully")

            return transformed_train_data, transformed_test_data

        except Exception as e:

            logging.error("Data transformation failed")

            raise CustomException(e, sys)