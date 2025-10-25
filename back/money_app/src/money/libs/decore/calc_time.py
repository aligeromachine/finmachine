import time
import logging
from functools import wraps
from money.libs.str.base import random_string
from typing import Callable, Any
from money.libs.types.exp import F_Return

logger = logging.getLogger(__name__)

def calculate_running_time(func: Callable[..., F_Return]) -> Callable[..., F_Return]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> F_Return:
        begin = time.time()
        random_name = random_string(5).lower()

        result = func(random_name, *args, **kwargs)
        end = time.time()

        elapsed = end - begin
        elapsed_min = int(elapsed // 60)
        elapsed_sec = int(elapsed % 60)

        logger.info(f"{random_name} Время выполнения {func.__name__} {elapsed_min} минут {elapsed_sec} секунд.")

        return result
    return wrapper
