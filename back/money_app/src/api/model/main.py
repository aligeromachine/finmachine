from functools import wraps
import logging
from typing import Callable
from pydantic import BaseModel
from django.http import HttpRequest
from money.libs.validate import validate_dict_conv

logger = logging.getLogger(__name__)

class MainModel(BaseModel):
    user_id: int = 0
    command: str

class FData(BaseModel):
    b64: str
    name: str
    type: str

def validate_model(Model: type[MainModel]): # type: ignore
    def decorator(func: Callable): # type: ignore
        @wraps(func)
        def wrapper(request: HttpRequest, *args: list, **kwargs: dict): # type: ignore

            data: MainModel = validate_dict_conv(request.body, Model=Model)
            if not data:
                return {'data': 'err', 'message': f'validate_dict_conv: {Model}'}

            data.user_id = request.user_id
            return func(request, data, *args, **kwargs)
        return wrapper
    return decorator

class ExtModel(MainModel):
    offset: int = 0
    limit: int = 0
    pk: int = 0
    title: str = ''
