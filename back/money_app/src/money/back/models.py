from functools import wraps
import logging
from typing import Callable
from pydantic import BaseModel, ValidationError
from django.http import HttpRequest
import orjson

from money.ext_func.ext_c import CONST

logger = logging.getLogger(__name__)

class MainModel(BaseModel):
    username: str = ''
    is_superuser: bool = False
    username_id: int = 0
    command: str = ''
    pk: int = 0

def parse_model(Model: type[MainModel]):
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(request: HttpRequest, *args, **kwargs):
            try:
                # Parse the request body into the Pydantic model
                data = Model(**orjson.loads(request.body))
                data.username = request.user.username
                data.is_superuser = bool(request.user.is_superuser)
                data.username_id = request.user.id
                # Pass the parsed data to the wrapped function
                return func(request, data, *args, **kwargs)
            except ValidationError as e:
                logger.error(e.json())
                return {"error": e.json()}
        return wrapper
    return decorator

class StatistMessage(MainModel):
    export_range_dt: str = CONST.empty

class StatPswMessage(MainModel):
    psw_update_login: str = CONST.empty
    psw_update_password: str = CONST.empty
    psw_update_hash: str = CONST.empty

    stat_psw_offset: int = 0
    stat_psw_limit: int = 0

class FData(BaseModel):
    b64: str
    name: str
    type: str

class ArhvMessage(MainModel):
    arhiv_update_file: FData | None = None
    arhiv_update_comment: str = CONST.empty

    arhiv_offset: int = 0
    arhiv_limit: int = 0

class SlovMessage(MainModel):
    slov_update_file: FData | None = None
    slov_update_comment: str = CONST.empty

    slov_offset: int = 0
    slov_limit: int = 0

class ProfileMessage(MainModel):
    new_password: str = CONST.empty


class LogMessage(MainModel):
    log_name: str = CONST.empty

class DashboardMessage(MainModel):
    dash_dt: str = CONST.empty

class ChartMessage(MainModel):
    chart_dt: str = CONST.empty

class ExchangeResolve(MainModel):
    exchange_resolve_input_file: FData | None = None
    download: int = 0


class HCtypes(MainModel):
    id: int
    name: str


