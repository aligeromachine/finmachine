from service.config.env import ENV_APP

CONFIG: dict = ENV_APP['CELERY']

HOST: str = CONFIG['HOST']
PORT: str = CONFIG['PORT']
BROKER: str = CONFIG['BROKER']
BACKEND: str = CONFIG['BACKEND']

CELERY_BROKER: str = f'{HOST}:{PORT}/1'
CELERY_BACKEND: str = f'{HOST}:{PORT}/2'
