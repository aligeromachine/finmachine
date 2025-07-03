from typing import Any, Self
from pydantic import BaseModel, model_validator
from money.libs.model import BaseModelWithRawArray
from decimal import Decimal

# SELECTOR DB
class SelectHash(BaseModel):
    id: int
    login: str
    hash: str

class SelectTask(BaseModel):
    id: int
    code: str
    hashes: list[SelectHash] = []

    @classmethod
    def from_raw_query(cls, raw_item: Any) -> Self:
        # Если данные уже в виде словаря
        if isinstance(raw_item, dict):
            return cls(**raw_item)

        # Если это объект ORM (например, Django или SQLAlchemy)
        if hasattr(raw_item, '__dict__'):
            return cls(**raw_item.__dict__)

        # Другие форматы можно добавить по необходимости
        raise ValueError(f"Unsupported raw item type: {type(raw_item)}")

    @model_validator(mode='after')
    def file_complete(self) -> Self:
        self.code = self.code.split("-")[0].strip()
        return self

class Payload(BaseModel):
    year: int
    buy: Decimal
    profit: Decimal

class BuyGroup(BaseModelWithRawArray):
    payload: list[Payload]
    user_id: int
