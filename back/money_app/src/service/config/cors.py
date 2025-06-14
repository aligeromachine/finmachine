from service.config.env import ENV_APP

CONFIG: dict = ENV_APP['SERVICE']

ALLOWED_HOSTS: str = str(CONFIG['ALLOWED']).split(",")
CORS_ALLOWED_ORIGINS: str = str(CONFIG['CORS']).split(",")
CORS_ALLOW_METHODS: list = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]
CORS_ALLOW_HEADERS: list = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]
CORS_ALLOW_CREDENTIALS: bool = True
