from pydantic import BaseModel
from api.back.decore import MainModel

LOG_DJANGO: str = 'django'
LOG_MONEY: str = 'money'
LOG_API: str = 'api'
LOG_ALL: str = 'all'

class LogMessage(MainModel):
    pass

class LogSignal(BaseModel):
    message: str | dict
    data: str = "ok"


class LogAllSignal(BaseModel):
    money: str
    api: str
    django: str
