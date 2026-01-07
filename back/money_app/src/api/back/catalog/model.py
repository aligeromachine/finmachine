from datetime import datetime
from typing import Self
from pydantic import model_validator
from api.back.decore import ExtModel
from libs.model.exp import BaseModelWithRawArray
from libs.dt.utils import pretty_str

class CatalogMessage(ExtModel):
    pass

class CatSignal(BaseModelWithRawArray):
    title: str
    created: datetime

class CatSignalKV(BaseModelWithRawArray):
    id: int
    title: str

class CatSelector(BaseModelWithRawArray):
    id: int
    created: datetime | str
    title: str

    @model_validator(mode='after')
    def complete(self) -> Self:
        if isinstance(self.created, datetime):
            self.created = pretty_str(self.created)
        return self
