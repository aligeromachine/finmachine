import os
from typing import Callable, Any
import requests
from functools import wraps
import logging
import urllib3
import pickle

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

logger = logging.getLogger(__name__)

def session_decorator(func: Callable[..., dict | list | bytes | None]) -> Callable[..., dict | list | bytes | None]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> dict | list | bytes | None:
        try:
            with requests.Session() as client:
                response: dict | list | bytes | None = func(client, *args, **kwargs)
                return response
        except requests.HTTPError as exc:
            logger.error(f"Session HTTP: {exc.request.url}")
        except Exception as exc:
            logger.error(f"Session An occurred: {exc}")
        return None
    return wrapper


def update_token(client: requests.Session) -> None:
    from money.libs.django.func import get_store_token
    if os.path.exists(get_store_token()):
        with open(get_store_token(), "rb") as f:
            client.cookies.update(pickle.load(f))

def dump_token(client: requests.Session) -> None:
    from money.libs.django.func import get_store_token
    if not os.path.exists(get_store_token()):
        with open(get_store_token(), "wb") as f:
            pickle.dump(client.cookies, f)

def session_token_decorator(func: Callable[..., dict | list | bytes | None]) -> Callable[..., dict | list | bytes | None]: # noqa
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> dict | list | bytes | None:
        try:
            with requests.Session() as client:
                update_token(client=client)
                response: dict | list | bytes | None = func(client, *args, **kwargs)
                dump_token(client=client)
                return response
        except requests.HTTPError as exc:
            logger.error(f"Session HTTP: {exc.request.url}")
        except Exception as exc:
            logger.error(f"Session An occurred: {exc}")
        return None
    return wrapper
