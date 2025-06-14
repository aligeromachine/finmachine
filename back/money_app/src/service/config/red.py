from service.config.env import ENV_APP

CONFIG: dict = ENV_APP['CELERY']

CELERY_BROKER: str = CONFIG['BROKER']
CELERY_BACKEND: str = CONFIG['BACKEND']

# CACHES = {
#     'default': {
#         'BACKEND': 'django_redis.cache.RedisCache',
#         'LOCATION': 'redis://127.0.0.1:6379/1',  # Replace with your Redis server address and database number
#         'OPTIONS': {
#             'CLIENT_CLASS': 'django_redis.client.DefaultClient',
#         }
#     }
# }

# SESSION_ENGINE = "django.contrib.sessions.backends.cache"
# SESSION_CACHE_ALIAS = "default"


# from django.core.cache import cache
# def get_data():
#     data = cache.get('my_data')
#     if data is None:
#         # Retrieve data from the database or another source
#         data = retrieve_data()
#         cache.set('my_data', data, timeout=3600)  # Cache for 1 hour
#     return data
