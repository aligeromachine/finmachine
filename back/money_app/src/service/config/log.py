from service.config.env import ENV_APP

CONFIG          = ENV_APP['LOG']

BASE_LOG        = '/home/data/media/log'

LOG_DJANGO      = 'django.log'
LOG_APP         = 'money.log'

ONE_MB = 1024 * 1024
BACKUP_COUNT = 2
LOG_LEVEL = CONFIG['LEVEL']

def create_fmt(fmt: str):
    return {
        "format": fmt,
        "datefmt": "%Y-%m-%d %H:%M:%S",
        "class": "logging.Formatter",
    }

def create_handler(fname: str, fmt: str):
    return {
        "level": LOG_LEVEL,
        "class": "logging.handlers.RotatingFileHandler",
        "filename": f'{BASE_LOG}/{fname}',
        "formatter": fmt,
        "maxBytes": ONE_MB,
        "backupCount": BACKUP_COUNT,
        "encoding": "utf-8",
    }

def create_file(fname: str):
    return {
        "handlers": [fname],
        "level": LOG_LEVEL,
        "propagate": True,
    }

def create_formatters():
    return {
        "generic": create_fmt(fmt="[%(asctime)s | %(levelname)-5s | %(name)-16s:%(lineno)-5d] %(message)-250s"),
        "simple": create_fmt(fmt="[%(asctime)s - %(name)s - %(levelname)s] - %(message)s"),
        "detailed": create_fmt(fmt="[%(asctime)s : %(levelname)s - %(name)s:%(lineno)d] - %(message)s"),
    }    

def create_handlers():
    return {
        "file_django": create_handler(fname=LOG_DJANGO, fmt="generic"),
        "file_money": create_handler(fname=LOG_APP, fmt="generic"),
    }    

def create_loggers():
    return {
        "django": create_file(fname="file_django"),
        "money": create_file(fname="file_money"),
    }   

LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": create_formatters(),
    "handlers": create_handlers(),
    "loggers": create_loggers(),
}
