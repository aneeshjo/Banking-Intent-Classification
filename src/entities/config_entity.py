from dataclasses import dataclass


@dataclass(frozen=True)
class DataIngestionConfig:
    train_data_file: str
    test_data_file: str

@dataclass(frozen=True)
class DataValidationConfig:
    schema_file: str


@dataclass(frozen=True)
class TfidfConfig:
    max_features: int
    ngram_range: tuple
    min_df: int
    max_df: float

@dataclass(frozen=True)
class DataTransformationConfig:
    text_column: str
    target_column: str
    lowercase: bool
    remove_extra_whitespace: bool
    tfidf:TfidfConfig
