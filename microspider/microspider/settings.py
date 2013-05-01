# how many times to retry when IOError happen
MAX_RETRY = 5

DATABASE_SERVER = ["219.223.220.20", "219.223.220.21", "219.223.220.22"]

# API_LOG = 
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "brief": {
            "format": "%(threadName)s:%(message)s",
            },
        "precise": {
            "format": "%(asctime)s - %(threadName)s - %(levelname)s: %(message)s",
            }
        },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "brief",
            "level": "INFO",
            },
        "error_file": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "error.log",
            "formatter": "precise",
            "level": "WARNING",
            "maxBytes": 1024*1024*10,
            "backupCount": 3,
            },
        "fetch_file": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "fetch.log",
            "formatter": "precise",
            "level": "INFO",
            "maxBytes": 1024*1024*10,
            "backupCount": 3,
            }
        },
    "loggers": {
        "fetch": {
            "handlers": ["console", "fetch_file"],
            "level": "INFO",
            "propagate": False,
            },
        "error": {
            "handlers": ["console", "error_file"],
            "level": "INFO",
            "propagate": False,
            }
        },
    }
