import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
ROOT_DIR = os.getcwd()

DIR_PATH = os.path.join(ROOT_DIR, "logs")
os.makedirs(DIR_PATH, exist_ok=True)

LOG_FILE_PATH = os.path.join(DIR_PATH, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format= '[ %(asctime)s ] - %(module)s - %(lineno)d - %(message)s - %(name)s ',
    level=logging.INFO
)