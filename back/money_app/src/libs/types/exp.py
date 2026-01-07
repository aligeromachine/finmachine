from typing import ParamSpec, TypeVar
from pydantic import BaseModel

TBaseModel = TypeVar('TBaseModel', bound='BaseModel')
F_Spec = ParamSpec("F_Spec")
F_Return = TypeVar("F_Return")
model_type = type[TBaseModel | dict | None]
