from datetime import datetime
from typing import Self
from pydantic import model_validator
from api.model.main import ExtModel
from money.libs.model import BaseModelWithRawArray
from money.libs.ext_utils import dateDRF

class ProductsMessage(ExtModel):
    catalog: int = 0

class ProdSignal(BaseModelWithRawArray):
    title: str
    catalog: int

class ProdSignalKV(BaseModelWithRawArray):
    id: int
    title: str

class ProdSelector(BaseModelWithRawArray):
    id: int
    created: datetime | str
    title: str
    catalog: str

    @model_validator(mode='after')
    def complete(self) -> Self:
        if isinstance(self.created, datetime):
            self.created = dateDRF(self.created)
        return self
