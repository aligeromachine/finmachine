from service.config.env import ENV_APP

CONFIG: dict = ENV_APP['CONNECT']

DATABASES: dict = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': CONFIG['NAME'],
        'USER': CONFIG['USER'],
        'PASSWORD': CONFIG['PASSWORD'],
        'HOST': CONFIG['HOST'],
        'PORT': CONFIG['PORT'],
        'OPTIONS': {
            'options': '-c search_path=public,content'
        }
    }
}
