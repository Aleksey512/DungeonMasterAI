import logging
import logging.config
import os

DEBUG = bool(int(os.getenv("DEBUG", False)))

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {"format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"},
        "detailed": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(pathname)s:%(lineno)d - %(message)s"
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "level": "INFO",
        },
    },
    "loggers": {
        "root": {"handlers": ["console"], "level": "INFO", "propagate": True},
        "uvicorn.error": {"handlers": ["console"], "level": "INFO", "propagate": True},
        "uvicorn.access": {"handlers": ["console"], "level": "INFO", "propagate": True},
        "watchfiles": {"level": "ERROR", "propagate": False},
    },
}


def setup_logging():
    config = LOGGING_CONFIG
    if DEBUG:
        config["handlers"]["console"]["level"] = "DEBUG"
        config["loggers"]["root"]["level"] = "DEBUG"
    logging.config.dictConfig(config)
    return config
