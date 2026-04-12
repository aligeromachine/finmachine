import logging
from functools import wraps
import orjson
from django.http import HttpRequest
from typing import Callable, Any
from pydantic import BaseModel, ValidationError
from libs.validate.exp import validate_dict_conv
from libs.types.exp import F_Return, F_Spec
from libs.django.jsonResponse import ORJSONResponse

logger = logging.getLogger(__name__)

def parse_api_model(Model: type[BaseModel]) -> Callable[F_Spec, Callable[F_Spec, F_Return | dict]]:  # type: ignore
    def decorator(func: Callable[F_Spec, F_Return | dict]) -> Callable[F_Spec, F_Return | dict]:  # type: ignore
        @wraps(func)
        def wrapper(request: HttpRequest, *args: F_Spec.args, **kwargs: F_Spec.kwargs) -> F_Return | dict:
            try:
                if not request.body:
                    return {'data': 'err', 'message': 'body empty'}
                return func(request, Model(**orjson.loads(request.body)), *args, **kwargs)
            except ValidationError as e:
                return {'data': 'err', 'message': e.json()}
        return wrapper
    return decorator

def token_response(token: dict | None = None, msg: str | None = None, code: int = 200) -> ORJSONResponse:
    return ORJSONResponse(data=dict(token=token, message=msg), status=code)

def check_post(view_func: Callable[..., ORJSONResponse]) -> ORJSONResponse:
    def wrapper_view(request: HttpRequest) -> ORJSONResponse:
        if request.method != 'POST':
            return token_response(msg='Method not allowed', code=405)
        return view_func(request)
    return wrapper_view

def validate_auth(Model: type[BaseModel]) -> ORJSONResponse:
    def decorator(func: Callable[..., ORJSONResponse]) -> ORJSONResponse:
        @wraps(func)
        def wrapper(request: HttpRequest, *args: Any, **kwargs: Any) -> ORJSONResponse:

            data: BaseModel = validate_dict_conv(response=request.body, Model=Model)
            if not data:
                return token_response(msg='Invalid data Model', code=400)
            return func(request, data, *args, **kwargs)
        return wrapper
    return decorator
