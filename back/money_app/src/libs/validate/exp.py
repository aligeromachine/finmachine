from typing import Any
import orjson
from pydantic import ValidationError
import logging
from libs.types.exp import TBaseModel

logger = logging.getLogger(__name__)

def to_json(data: dict, prn: bool = False) -> Any:
    if not data:
        return None

    try:
        return orjson.dumps(data).decode('utf-8')
    except Exception as e:
        if prn: 
            logger.error(f'{str(e)}, {data=}')
        return None

def validate_conv(response: str, prn: bool = False) -> Any:
    if not response:
        return None

    try: 
        return orjson.loads(response)
    except Exception as e:
        if prn: 
            logger.error(f'{str(e)}, {response=}')
        return None

def validate_dict(response: dict, Model: type[TBaseModel], prn: bool = True) -> TBaseModel | None:
    if not response:
        return None
    if not isinstance(response, dict):
        return None

    try:
        data = Model(**response)
        return data
    except ValidationError as e:
        if prn: 
            logger.error(f'{e.json()}, {response=}, {Model=}')
        return None

def validate_list(response: list, Model: type[TBaseModel], prn: bool = True) -> list | None:
    if not response:
        return None
    if not isinstance(response, list):
        return None

    try:
        return [Model(**it) for it in response]
    except ValidationError as e:
        if prn: 
            logger.error(f'{e.json()}, {response=}, {Model=}')
        return None

def validate_dict_conv(response: str, Model: type[TBaseModel], prn: bool = True) -> TBaseModel | None:
    if not response:
        return None

    try: 
        return validate_dict(response=orjson.loads(response), Model=Model, prn=False)
    except Exception as e:
        if prn: 
            logger.error(f'{str(e)}, {response=}, {Model=}')
        return None

def validate_list_conv(response: str, Model: type[TBaseModel], prn: bool = True) -> list | None:
    if not response:
        return None

    try: 
        return validate_list(response=orjson.loads(response), Model=Model, prn=False)
    except Exception as e:
        if prn: 
            logger.error(f'{str(e)}, {response=}, {Model=}')
        return None

def validate_dict_list(response: dict, Model: type[TBaseModel], key: str, prn: bool = True) -> list | None:
    if key not in response:
        return None

    try:
        sub = response[key]
        return validate_list(response=sub, Model=Model, prn=False)
    except Exception as e:
        if prn: 
            logger.error(f'{str(e)}, {response=}, {Model=}')
        return None

def validate_str(response: bytes, prn: bool = True) -> str | None:
    if not response:
        return None

    if not isinstance(response, bytes):
        return None

    try:
        return response.decode()
    except Exception as e:
        if prn: 
            logger.error(f'{str(e)}, {response=}')
        return None
