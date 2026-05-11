from src.entity.config_entity import DataIngestionConfig
from src.exception import DLClassifierException
from src.logging import logging
import sys

from src.utils.main_utils import read_yaml, create_directories, get_size
from src.constants import *

import os
import urllib.request as request
import zipfile

class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config = config
    
    def download_file(self):
        try:
            if not os.path.exists(self.config.local_data_file):
                filename, headers = request.urlretrieve(
                    url = self.config.source_URL,
                    filename= self.config.local_data_file
                )
                logging.info(f"{filename} Downloaded with following info : \n{headers}")
            else:
                logging.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")
        except Exception as e:
            logging.error(e)
            raise DLClassifierException(e, sys)
    
    def extract_zipfile(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip:
            zip.extractall(unzip_path)
