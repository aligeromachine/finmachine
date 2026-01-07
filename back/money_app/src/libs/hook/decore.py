import functools
from typing import Any, Callable
from libs.types.exp import F_Return, F_Spec


def hook(before: str = '', after: str = '') -> Callable[[Callable], Callable]:
    """Декоратор‑хук для методов экземпляра."""
    def decorator(func: Callable[..., F_Return]) -> Callable[..., F_Return]:
        @functools.wraps(func)
        def wrapper(self: Any, *args: F_Spec.args, **kwargs: F_Spec.kwargs) -> F_Return:
            if before:
                pre = getattr(self, before, None)
                if callable(pre):
                    pre(*args, **kwargs)

            result = func(self, *args, **kwargs)

            if after:
                post = getattr(self, after, None)
                if callable(post):
                    post(result, *args, **kwargs)

            return result
        return wrapper
    return decorator
