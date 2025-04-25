import orjson
from pydantic import BaseModel, ValidationError
import logging

logger = logging.getLogger(__name__)

def validate_dict(response: dict, Model: type[BaseModel], prn: bool = False):
    try:
        data = Model(**response)
        return data
    except ValidationError as e:
        if prn: 
            logger.error(f'{e.json()}, {response=}, {Model=}')
        return None

def validate_list(response: list, Model: type[BaseModel], prn: bool = False):
    try:
        return [Model(**it) for it in response]
    except ValidationError as e:
        if prn: 
            logger.error(f'{e.json()}, {response=}, {Model=}')
        return None

def validate_dict_conv(response: str, Model: type[BaseModel], prn: bool = False):
    try: 
        return validate_dict(response=orjson.loads(response), Model=Model)
    except Exception as e:
        if prn: 
            logger.error(f'{str(e)}, {response=}, {Model=}')
        return None

def validate_list_conv(response: str, Model: type[BaseModel], prn: bool = False):
    try: 
        return validate_list(response=orjson.loads(response), Model=Model, prn=False)
    except Exception as e:
        if prn: 
            logger.error(f'{str(e)}, {response=}, {Model=}')
        return None

def validate_dict_list(response: dict, Model: type[BaseModel], key: str, prn: bool = False):

    if key not in response:
        return None

    try:
        sub = response[key]
        return validate_list(response=sub, Model=Model, prn=False)
    except Exception as e:
        if prn: 
            logger.error(f'{str(e)}, {response=}, {Model=}')
        return None

def validate_str(response: bytes, prn: bool = False):

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

    return None
