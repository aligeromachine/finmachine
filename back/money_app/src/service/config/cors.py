from service.config.env import ENV_APP

CONFIG                  = ENV_APP['SERVICE']

ALLOWED_HOSTS           = str(CONFIG['ALLOWED']).split(",")
CORS_ALLOWED_ORIGINS    = str(CONFIG['CORS']).split(",")
CORS_ALLOW_METHODS      = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]
CORS_ALLOW_HEADERS      = [
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
CORS_ALLOW_CREDENTIALS  = True
