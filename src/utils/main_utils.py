from box import ConfigBox
import yaml
from pathlib import Path
import os
import sys
import json
import joblib
import base64
from src.logging import logging
from src.exception import DLClassifierException

from typing import Any

def read_yaml(yaml_path:Path) -> ConfigBox:
    try:
        with open(yaml_path, 'r', encoding='utf-8') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info("YAML file Successfully Loaded")

            if content is None:
                raise ValueError("❌ YAML file is empty or badly formatted.")
            
            return ConfigBox(content)
        
    except Exception as e:
        logging.error(e)
        raise DLClassifierException(e, sys)

def create_directories(directory_path: list, verbose=True):
    for path in directory_path:
        os.makedirs(path, exist_ok=True)

        if verbose:
            logging.info(f"Created Directory at: {path}")

def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logging.info(f"json file saved at: {path}")




# @ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logging.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)


# @ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logging.info(f"binary file saved at: {path}")


# @ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logging.info(f"binary file loaded from: {path}")
    return data

# @ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"


def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())