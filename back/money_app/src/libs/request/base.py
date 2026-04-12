import orjson
import requests
import urllib3
import logging
from libs.request.http import session_decorator
from libs.const import HEADERS, TIMEOUT
from libs.decore.lam import dump_model
from libs.types.exp import TBaseModel

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
logger = logging.getLogger(__name__)

@session_decorator  # type: ignore
def get_data(client: requests.Session, url: str, data: TBaseModel | dict | None = None) -> dict | list:
    response = client.get(
        url, 
        params=dump_model(data),            
        headers=HEADERS,
        timeout=TIMEOUT,
        verify=False,
    )
    respo: dict | list = orjson.loads(response.content)
    return respo

@session_decorator  # type: ignore
def post_data(client: requests.Session, url: str, data: TBaseModel | dict | None = None) -> dict | list:
    response = client.post(
        url, 
        json=dump_model(data),
        headers=HEADERS,
        timeout=TIMEOUT,
        verify=False,
    )
    respo: dict | list = orjson.loads(response.content)
    return respo

@session_decorator  # type: ignore
def patch_data(client: requests.Session, url: str, data: TBaseModel | dict | None = None) -> dict | list:
    response = client.patch(
        url, 
        json=dump_model(data),
        headers=HEADERS,
        timeout=TIMEOUT,
        verify=False,
    )
    respo: dict | list = orjson.loads(response.content)
    return respo

@session_decorator  # type: ignore
def delete_data(client: requests.Session, url: str, data: TBaseModel | dict | None = None) -> dict | list:
    response = client.delete(
        url, 
        params=dump_model(data),            
        headers=HEADERS,
        timeout=TIMEOUT,
        verify=False,
    )
    respo: dict | list = orjson.loads(response.content)
    return respo

@session_decorator  # type: ignore 
def get_ctx(client: requests.Session, url: str, data: TBaseModel | dict | None = None) -> bytes:
    response = client.get(
        url, 
        params=dump_model(data),
        headers=HEADERS,
        timeout=TIMEOUT,
        verify=False,
    )

    respo: bytes = response.content
    return respo

@session_decorator  # type: ignore
def resume_download(client: requests.Session, url: str) -> bytes:
    block_size = 1024 * 500
    binary_content = b""
    current_size = 0

    while True:

        headers = {'Range': f'bytes={current_size}-'}
        response = client.get(
            url,
            stream=True,
            headers=headers,
            timeout=TIMEOUT,
            verify=False,
        )

        response.raise_for_status()
        for chunk in response.iter_content(chunk_size=block_size, decode_unicode=True):

            read_data: bytes = bytes(chunk)

            if not read_data:
                the_end = True
                break

            binary_content += read_data
            current_size += block_size

        if the_end:
            break

    return binary_content
