from service.config.env import ENV_APP

CONFIG: dict = ENV_APP['CELERY']

CELERY_BROKER: str = CONFIG["BROKER"]
CELERY_BACKEND: str = CONFIG["BACKEND"]