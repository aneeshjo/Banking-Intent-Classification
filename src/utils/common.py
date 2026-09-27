import os
import yaml


def read_yaml(path):
    """
    Read a YAML file and return its contents as a dictionary.
    """
    with open(path, "r") as file:
        return yaml.safe_load(file)


def create_directories(paths):
    """
    Create directories if they do not already exist.
    """
    for path in paths:
        os.makedirs(path, exist_ok=True)