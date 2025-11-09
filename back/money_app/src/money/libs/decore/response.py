import logging
from functools import wraps
import orjson
from django.http import HttpRequest, JsonResponse
from typing import Callable, Any
from pydantic import BaseModel, ValidationError
from money.libs.validate.exp import validate_dict_conv
from money.libs.types.exp import F_Return

logger = logging.getLogger(__name__)

def parse_api_model(Model: type[BaseModel]) -> Callable[..., Callable[..., F_Return | dict]]:
    def decorator(func: Callable[..., F_Return | dict]) -> Callable[..., F_Return | dict]:
        @wraps(func)
        def wrapper(request: HttpRequest, *args: Any, **kwargs: Any) -> F_Return | dict:
            try:
                if not request.body:
                    return {'data': 'err', 'message': 'body empty'}
                return func(request, Model(**orjson.loads(request.body)), *args, **kwargs)
            except ValidationError as e:
                return {'data': 'err', 'message': e.json()}
        return wrapper
    return decorator

def token_response(token: dict | None = None, msg: str | None = None, code: int = 200) -> JsonResponse:
    return JsonResponse({'token': token, 'message': msg}, status=code)

def check_post(view_func: Callable[..., JsonResponse]) -> JsonResponse:
    def wrapper_view(request: HttpRequest) -> JsonResponse:
        if request.method != 'POST':
            return token_response(msg='Method not allowed', code=405)
        return view_func(request)
    return wrapper_view

def validate_auth(Model: type[BaseModel]) -> JsonResponse:
    def decorator(func: Callable[..., JsonResponse]) -> JsonResponse:
        @wraps(func)
        def wrapper(request: HttpRequest, *args: Any, **kwargs: Any) -> JsonResponse:

            data: BaseModel = validate_dict_conv(response=request.body, Model=Model)
            if not data:
                return token_response(msg='Invalid data Model', code=400)
            return func(request, data, *args, **kwargs)
        return wrapper
    return decorator
