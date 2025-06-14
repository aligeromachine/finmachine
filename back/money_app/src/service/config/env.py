import os


def get_env(key: str, conv: bool = False) -> str | bool:
    if conv:
        return bool(int(os.environ.get(key)))
    return os.environ.get(key)

def create_connect() -> dict:
    return {
        'NAME': get_env('POSTGRES_NAME'),
        'USER': get_env('POSTGRES_USER'),
        'PASSWORD': get_env('POSTGRES_PASSWORD'),
        'HOST': get_env('POSTGRES_HOST'),
        'PORT': get_env('POSTGRES_PORT'),
    }

def create_service() -> dict:
    return {
        'DEBUG': get_env('SERVICE_DEBUG', True),
        'KEY': get_env('SERVICE_KEY'),
        'ALLOWED': get_env('SERVICE_ALLOWED'),
        'CORS': get_env('SERVICE_CORS'),
    }

def create_log() -> dict:
    return {
        "LEVEL": get_env('LOG_LEVEL'),
    }

def create_celery() -> dict:
    return {
        'BROKER': get_env('CELERY_BROKER'),
        'BACKEND': get_env('CELERY_BACKEND'),
    }

def create_money() -> dict:
    return {
        'EXPIRED': get_env('MONEY_EXPIRED'),
    }

def create_jwt() -> dict:
    return {
        'SECRET_KEY': get_env('JWT_SECRET_KEY'),
        'ALGORITHM_JWT': get_env('JWT_ALGORITHM'),
        'ACCESS_LIFETIME': get_env('JWT_ACCESS_LIFETIME'),
        'REFRESH_LIFETIME': get_env('JWT_REFRESH_LIFETIME'),
    }


ENV_APP: dict = {    
    'CONNECT': create_connect(),
    'SERVICE': create_service(),
    'LOG': create_log(),
    'CELERY': create_celery(),
    'MONEY': create_money(),
    'AUTH': create_jwt(),
}
