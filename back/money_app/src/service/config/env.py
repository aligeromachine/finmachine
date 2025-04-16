import os

def get_env(key: str, conv: bool = False):
    if conv:
        return bool(int(os.environ.get(key)))
    
    return os.environ.get(key)

def create_log():
    return {
        "LEVEL":            get_env('LOG_LEVEL'),
    }

def create_connect():
    return {
        'NAME':             get_env('POSTGRES_NAME'),
        'USER':             get_env('POSTGRES_USER'),
        'PASSWORD':         get_env('POSTGRES_PASSWORD'),
        'HOST':             get_env('POSTGRES_HOST'),
        'PORT':             get_env('POSTGRES_PORT'),
    }

def create_celery():
    return {
        'BROKER':           get_env('CELERY_BROKER'),
        'BACKEND':          get_env('CELERY_BACKEND'),
    }

def create_money():
    return {
        'EXPIRED':          get_env('MONEY_EXPIRED'),
    }

def create_service():
    return {
        'DEBUG':            get_env('SERVICE_DEBUG', True),
        'KEY':              get_env('SERVICE_KEY'),
        'ALLOWED':          get_env('SERVICE_ALLOWED'),
        'CORS':             get_env('SERVICE_CORS'),
    }

ENV_APP = {
    'LOG':                  create_log(),
    'CONNECT':              create_connect(),
    'CELERY':               create_celery(),
    'MONEY':                create_money(),
    'SERVICE':              create_service(),
}
