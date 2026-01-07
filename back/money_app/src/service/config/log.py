from service.config.env import ENV_APP

CONFIG: dict = ENV_APP['LOG']

BASE_LOG: str = '/home/data/media/log'


LOG_DJANGO: str = 'django'
LOG_MONEY: str = 'money'
LOG_AUTH: str = 'auth'
LOG_API: str = 'api'
LOG_LIBS: str = 'libs'

ONE_MB: int = 1024 * 1024
BACKUP_COUNT: int = 2
LOG_LEVEL: str = CONFIG['LEVEL']

def create_fmt(fmt: str) -> dict:
    return {
        "format": fmt,
        "datefmt": "%Y-%m-%d %H:%M:%S",
        "class": "logging.Formatter",
    }

def create_handler(fname: str, fmt: str) -> dict:
    return {
        "level": LOG_LEVEL,
        "class": "logging.handlers.RotatingFileHandler",
        "filename": f'{BASE_LOG}/{fname}.log',
        "formatter": fmt,
        "maxBytes": ONE_MB,
        "backupCount": BACKUP_COUNT,
        "encoding": "utf-8",
    }

def create_file(fname: str) -> dict:
    return {
        "handlers": [fname],
        "level": LOG_LEVEL,
        "propagate": True,
    }

def create_formatters() -> dict:
    return {
        "generic": create_fmt(fmt="[%(asctime)s | %(levelname)-5s | %(name)-16s:%(lineno)-5d] %(message)-250s"),
        "simple": create_fmt(fmt="[%(asctime)s - %(name)s - %(levelname)s] - %(message)s"),
        "detailed": create_fmt(fmt="[%(asctime)s : %(levelname)s - %(name)s:%(lineno)d] - %(message)s"),
    }    

def create_handlers() -> dict:
    return {
        "file_django": create_handler(fname=LOG_DJANGO, fmt="generic"),
        "file_money": create_handler(fname=LOG_MONEY, fmt="generic"),
        "file_auth": create_handler(fname=LOG_AUTH, fmt="generic"),
        "file_api": create_handler(fname=LOG_API, fmt="generic"),
        "file_libs": create_handler(fname=LOG_LIBS, fmt="generic"),
    }    

def create_loggers() -> dict:
    return {
        "django": create_file(fname="file_django"),
        "money": create_file(fname="file_money"),
        "authentication": create_file(fname="file_auth"),
        "api": create_file(fname="file_api"),
        "libs": create_file(fname="file_libs"),
    }   


LOGGING: dict = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": create_formatters(),
    "handlers": create_handlers(),
    "loggers": create_loggers(),
}
