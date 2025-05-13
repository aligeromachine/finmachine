from functools import wraps
import time
from typing import Callable, Any
from django.http import HttpRequest, JsonResponse
from pydantic import BaseModel

from money.libs.ext_utils import RandomName
from money.libs.validate import validate_dict_conv
import logging

logger = logging.getLogger(__name__)

def token_response(token: dict | None = None, msg: str | None = None, code: int = 200) -> JsonResponse:
    return JsonResponse({'token': token, 'message': msg}, status=code)

def check_post(view_func: Callable) -> Any:
    def wrapper_view(request: HttpRequest) -> Any:
        if request.method != 'POST':
            return token_response(msg='Method not allowed', code=405)
        return view_func(request)
    return wrapper_view

def validate_auth(Model: type[BaseModel]) -> Any:
    def decorator(func: Callable) -> Any:
        @wraps(func)
        def wrapper(request: HttpRequest, *args: list, **kwargs: dict) -> Any:

            data: BaseModel = validate_dict_conv(response=request.body, Model=Model)
            if not data:
                return token_response(msg='Invalid data Model', code=400)
            return func(request, data, *args, **kwargs)
        return wrapper
    return decorator

def calculate_running_time(func: Callable) -> Any:
    @wraps(func)
    def wrapper(*args: list, **kwargs: dict) -> Any:
        begin = time.time()
        random_name = RandomName(5).lower()

        result = func(random_name, *args, **kwargs)
        end = time.time()

        elapsed = end - begin
        elapsed_min = int(elapsed // 60)
        elapsed_sec = int(elapsed % 60)

        logger.info(f"{random_name} Время выполнения {func.__name__} {elapsed_min} минут {elapsed_sec} секунд.")

        return result
    return wrapper
