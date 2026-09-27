import os
from pathlib import Path


project_name = "Banking Intent Classification"


list_of_files = [

    "config/__init__.py",

    "dataset/raw/.gitkeep",

    "artifacts/.gitkeep",

    "notebooks/.gitkeep",

    "src/__init__.py",
    "src/components/__init__.py",
    "src/config/__init__.py",
    "src/entities/__init__.py",
    "src/pipeline/__init__.py",
    "src/utils/__init__.py",

    "tests/__init__.py",

    "logs/.gitkeep",

    "requirements.txt",
    "setup.py",
    "README.md",
    ".gitignore",
]


for file_path in list_of_files:

    file_path = Path(file_path)

    file_directory = file_path.parent

    if file_directory != Path(""):
        os.makedirs(file_directory, exist_ok=True)

    if not file_path.exists():
        file_path.touch()

        print(f"Created: {file_path}")

    else:
        print(f"Already exists: {file_path}")