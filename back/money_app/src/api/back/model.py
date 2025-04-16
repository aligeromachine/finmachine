from functools import wraps
from typing import Callable
from pydantic import ValidationError, BaseModel
from django.http import HttpRequest
import orjson


def parse_model(Model: type[BaseModel]):
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(request: HttpRequest, *args, **kwargs):
            try:
                data = Model(**orjson.loads(request.body))
                return func(request, data, *args, **kwargs)
            except ValidationError as e:
                return {'data': 'err', 'message': e.json()}
        return wrapper
    return decorator


class Hashes(BaseModel):
    hashes: str
    hashtype: str
    iden: str
    cipher: str


class MetaComment(BaseModel):
    username: str
    command: str
    payload: Hashes | int
