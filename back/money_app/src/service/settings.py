from .config.index import SECRET_KEY_RAW, DEBUG_RAW, INSTALLED_APPS_RAW, MIDDLEWARE_RAW, \
    TEMPLATES_RAW, DATABASES_RAW, AUTH_PASSWORD_VALIDATORS_RAW, AUTHENTICATION_BACKENDS_RAW, \
    ALLOWED_HOSTS_RAW, CORS_ALLOWED_ORIGINS_RAW, CELERY_BROKER_RAW, CELERY_BACKEND_RAW, \
    LOGGING_RAW, ENV_APP_RAW, CORS_ALLOW_METHODS_RAW, CORS_ALLOW_HEADERS_RAW, CORS_ALLOW_CREDENTIALS_RAW

VERSION = '0.3.5'

ENV_APP = ENV_APP_RAW
DEBUG = DEBUG_RAW
SECRET_KEY = SECRET_KEY_RAW
INSTALLED_APPS = INSTALLED_APPS_RAW
MIDDLEWARE = MIDDLEWARE_RAW
TEMPLATES = TEMPLATES_RAW
DATABASES = DATABASES_RAW
CELERY_BROKER = CELERY_BROKER_RAW
CELERY_BACKEND = CELERY_BACKEND_RAW
AUTH_PASSWORD_VALIDATORS = AUTH_PASSWORD_VALIDATORS_RAW
AUTHENTICATION_BACKENDS = AUTHENTICATION_BACKENDS_RAW
ALLOWED_HOSTS = ALLOWED_HOSTS_RAW
LOGGING = LOGGING_RAW
CORS_ALLOWED_ORIGINS = CORS_ALLOWED_ORIGINS_RAW
CORS_ALLOW_METHODS = CORS_ALLOW_METHODS_RAW
CORS_ALLOW_HEADERS = CORS_ALLOW_HEADERS_RAW
CORS_ALLOW_CREDENTIALS = CORS_ALLOW_CREDENTIALS_RAW

ROOT_URLCONF = 'service.urls'
WSGI_APPLICATION = 'service.wsgi.application'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = False
MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/data/media/'
STATIC_URL = '/static/'
STATIC_ROOT = '/home/data/static/'
DATA_UPLOAD_MAX_MEMORY_SIZE = 10 * 1_024_000
LOGIN_REDIRECT_URL, LOGOUT_REDIRECT_URL, LOGIN_URL = 'dashboard', 'login', 'login/'
