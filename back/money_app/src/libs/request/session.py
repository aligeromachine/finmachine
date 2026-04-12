import orjson
import requests
import urllib3
from libs.const import HEADERS_MOZILA, TIMEOUT, PROXY_CRUSH
from libs.request.http import session_token_decorator
from libs.types.exp import TBaseModel
from libs.decore.lam import dump_model

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

@session_token_decorator  # type: ignore
def get_content(client: requests.Session, url: str, data: TBaseModel | dict | None = None, headers: dict = HEADERS_MOZILA) -> bytes:
    response = client.get(
        url, 
        params=dump_model(data),            
        headers=headers,
        timeout=TIMEOUT,
        verify=False,
    )
    respo: bytes = response.content
    return respo

@session_token_decorator  # type: ignore
def get_json(client: requests.Session, url: str, data: TBaseModel | dict | None = None, headers: dict = HEADERS_MOZILA) -> dict | list:
    response = client.get(
        url, 
        params=data,            
        headers=headers,
        timeout=TIMEOUT,
        verify=False,
    )

    respo: dict | list = orjson.loads(response.content)
    return respo

@session_token_decorator  # type: ignore
def post_file(client: requests.Session, url: str, files: dict, headers: dict = HEADERS_MOZILA) -> bytes:
    response = client.post(
        url, 
        files=files,
        headers=headers,
        timeout=TIMEOUT,
        verify=False,
    )

    respo: bytes = response.content
    return respo

@session_token_decorator  # type: ignore
def post_file_data(client: requests.Session, url: str, data: TBaseModel | dict | None = None, headers: dict = HEADERS_MOZILA) -> dict | list:
    response = client.post(
        url, 
        data=data,
        headers=headers,
        timeout=TIMEOUT,
        verify=False,
    )

    respo: dict | list = orjson.loads(response.content)
    return respo

@session_token_decorator  # type: ignore
def get_text(client: requests.Session, url: str, data: TBaseModel | dict | None = None, headers: dict = HEADERS_MOZILA) -> str:
    response = client.get(
        url, 
        params=data,
        headers=headers,
        timeout=TIMEOUT,
        verify=False,
    )

    return response.text

@session_token_decorator  # type: ignore
def post_data(client: requests.Session, url: str, data: TBaseModel | dict | None = None, headers: dict = HEADERS_MOZILA) -> dict | list:
    response = client.post(
        url, 
        json=data,
        headers=headers,
        timeout=TIMEOUT,
        verify=False,
    )

    respo: dict | list = orjson.loads(response.content)
    return respo

@session_token_decorator  # type: ignore
def patch_data(client: requests.Session, url: str, data: TBaseModel | dict | None = None, headers: dict = HEADERS_MOZILA) -> dict | list:
    response = client.patch(
        url, 
        json=data,
        headers=headers,
        timeout=TIMEOUT,
        verify=False,
    )

    respo: dict | list = orjson.loads(response.content)
    return respo

@session_token_decorator  # type: ignore
def delete_data(client: requests.Session, url: str, data: TBaseModel | dict | None = None, headers: dict = HEADERS_MOZILA) -> dict | list:
    response = client.delete(
        url, 
        params=data,            
        headers=headers,
        timeout=TIMEOUT,
        verify=False,
    )

    respo: dict | list = orjson.loads(response.content)
    return respo

@session_token_decorator  # type: ignore
def get_proxy_cont(client: requests.Session, url: str, data: TBaseModel | dict | None = None, headers: dict = HEADERS_MOZILA) -> str:
    response = client.get(
        url, 
        params=data,
        headers=headers,
        timeout=TIMEOUT,
        verify=False,
        proxies=PROXY_CRUSH,
    )
    return response.text

@session_token_decorator  # type: ignore
def post_proxy_cont(client: requests.Session, url: str, data: TBaseModel | dict | None = None, headers: dict = HEADERS_MOZILA) -> dict | list:
    response = client.post(
        url, 
        json=data,
        headers=headers,
        timeout=TIMEOUT,
        verify=False,
        proxies=PROXY_CRUSH
    )
    respo: dict | list = orjson.loads(response.content)
    return respo
