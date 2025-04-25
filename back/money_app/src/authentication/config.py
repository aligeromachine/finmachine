import datetime
from service.settings import ENV_APP

CONFIG                  = ENV_APP['AUTH']

# Настройки JWT

SECRET_KEY              = CONFIG['SECRET_KEY'] # noqa
ALGORITHM               = CONFIG['ALGORITHM_JWT'] 
ACCESS_LIFETIME         = datetime.timedelta(minutes=int(CONFIG['ACCESS_LIFETIME']))
REFRESH_LIFETIME        = datetime.timedelta(days=int(CONFIG['REFRESH_LIFETIME']))
