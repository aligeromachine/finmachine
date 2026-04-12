from libs.request.base import get_data, post_data, patch_data, delete_data, get_ctx
from libs.types.exp import TBaseModel

def get_x(url: str, data: TBaseModel | dict | None = None) -> list | dict | None:
    try:
        return get_data(url=url, data=data)  # type: ignore
    except: # noqa
        return None

def post_x(url: str, data: TBaseModel | dict | None = None) -> list | dict | None:
    try:
        return post_data(url=url, data=data)  # type: ignore
    except: # noqa
        return None

def patch_x(url: str, data: TBaseModel | dict | None = None) -> list | dict | None:
    try:
        return patch_data(url=url, data=data)  # type: ignore
    except: # noqa
        return None

def delete_x(url: str, data: TBaseModel | dict | None = None) -> list | dict | None:
    try:
        return delete_data(url=url, data=data)  # type: ignore
    except: # noqa
        return None

def get_xc(url: str, data: TBaseModel | dict | None = None) -> bytes | None:
    try:
        return get_ctx(url=url, data=data)  # type: ignore
    except: # noqa
        return None
