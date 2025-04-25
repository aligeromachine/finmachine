from functools import wraps
import time
from typing import Callable
from django.http import HttpRequest, JsonResponse
from pydantic import BaseModel

from money.libs.ext_utils import RandomName
from money.libs.validate import validate_dict_conv
import logging

logger = logging.getLogger(__name__)

def token_response(token: dict = None, msg: str = None, code: int = 200):
    return JsonResponse({'token': token, 'message': msg}, status=code)

def check_post(view_func):
    def wrapper_view(request: HttpRequest):

        if request.method != 'POST':
            return token_response(msg='Method not allowed', code=405)
        return view_func(request)
    return wrapper_view

def validate_auth(Model: type[BaseModel]):
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(request: HttpRequest, *args, **kwargs):

            data: BaseModel = validate_dict_conv(response=request.body, Model=Model)
            if not data:
                return token_response(msg='Invalid data Model', code=400)
            return func(request, data, *args, **kwargs)
        return wrapper
    return decorator

def calculate_running_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
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