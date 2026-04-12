from service.settings import ENV_APP

CONFIG = ENV_APP['MONEY']

REDIS_HOST: str = CONFIG['HOST']
REDIS_PORT: int = int(CONFIG['PORT'])
CACHE_BASE: int = int(CONFIG['BASE'])
EXPIRED: str = CONFIG['EXPIRED']
