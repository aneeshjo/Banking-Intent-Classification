from dataclasses import dataclass


@dataclass(frozen=True)
class DataIngestionConfig:
    train_data_file: str
    test_data_file: str