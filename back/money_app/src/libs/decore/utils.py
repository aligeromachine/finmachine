from functools import wraps
from typing import Callable
from libs.types.exp import F_Spec

def draw_paginate(func: Callable[F_Spec, dict]) -> Callable[F_Spec, dict]:  # type: ignore
    @wraps(func)
    def wrapper(*args: F_Spec.args, **kwargs: F_Spec.kwargs) -> dict:
        ls, count, offset, limit = func(*args, **kwargs)
        result = dict(
            recordsTotal=count,
            offset=offset,
            recordsDisplay=limit,
            draw=ls
        )
        return result
    return wrapper
