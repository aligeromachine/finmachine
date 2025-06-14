from service.config.env import ENV_APP

CONFIG: dict = ENV_APP['SERVICE']

DEBUG: str = CONFIG['DEBUG']
