import json
import logging
import logging.config
import os
from pathlib import Path

DEBUG = bool(int(os.getenv("DEBUG", False)))

LOG_CONFIG_FILE = Path(__file__).parent / "logging_config.json"


def setup_logging():
    with LOG_CONFIG_FILE.open() as f:
        config = json.load(f)
    if DEBUG:
        config["handlers"]["console"]["level"] = "DEBUG"
        config["loggers"]["root"]["level"] = "DEBUG"
    logging.config.dictConfig(config)
    return config
