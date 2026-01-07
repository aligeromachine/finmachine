from datetime import datetime
from typing import Self
from pydantic import Field, model_validator
from api.back.decore import ExtModel
from libs.model.exp import BaseModelWithRawArray
from libs.dt.utils import pretty_str

class ProductsMessage(ExtModel):
    catalog: int = 0

class ProdSignal(BaseModelWithRawArray):
    title: str
    catalog: int = Field(..., alias="catalog_id")
    created: datetime

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
            self.created = pretty_str(self.created)
        return self
