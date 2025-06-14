from service.config.env import ENV_APP

CONFIG: dict = ENV_APP['SERVICE']

SECRET_KEY: str = CONFIG['KEY']
