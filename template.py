import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s:")
project_name = 'CatvsDog'
files_list = [
    '.github/workflows/.gitkeep',
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constant/__init__.py",
    'config/config.yaml',
    'research/practice.ipynb',
    'requirements.txt',
    'setup.py',
    'params.yaml'
]

for filepath in files_list:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir:
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'Creating directory {filedir} for file: {filename}')

    if (not os.path.exists(filepath) or os.path.getsize(filepath) != 0):
        with open(filepath, 'w') as f:
            pass

    else:
        logging.info(f'{filename} is already exist')