from datetime import datetime
from typing import Self
from pydantic import model_validator
from api.model.main import ExtModel
from money.libs.model import BaseModelWithRawArray
from money.libs.ext_utils import dateDRF

class ShopMessage(ExtModel):
    address: str = ''

class ShopSignal(BaseModelWithRawArray):
    title: str
    address: str

class ShopSignalKV(BaseModelWithRawArray):
    pk: int
    title: str

class ShopSelector(BaseModelWithRawArray):
    id: int
    created: datetime | str
    title: str
    address: str

    @model_validator(mode='after')
    def complete(self) -> Self:
        if isinstance(self.created, datetime):
            self.created = dateDRF(self.created)
        return self
