import logging
import sys

from backend.app.configuration import config


logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


def get_logger(name=config.DEFAULT_LOG_NAME):
    return logging.getLogger(name)
