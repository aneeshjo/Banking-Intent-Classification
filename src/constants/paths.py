from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[2]

CONFIG_DIR = ROOT_DIR / "config"

CONFIG_FILE_PATH = CONFIG_DIR / "config.yaml"
PARAMS_FILE_PATH = CONFIG_DIR / "params.yaml"
SCHEMA_FILE_PATH = CONFIG_DIR / "schema.yaml"

DATASET_DIR = ROOT_DIR / "Dataset"
RAW_DATA_DIR = DATASET_DIR / "raw"

TRAIN_DATA_PATH = RAW_DATA_DIR / "train.csv"
TEST_DATA_PATH = RAW_DATA_DIR / "test.csv"

ARTIFACTS_DIR = ROOT_DIR / "artifacts"
LOGS_DIR = ROOT_DIR / "logs"