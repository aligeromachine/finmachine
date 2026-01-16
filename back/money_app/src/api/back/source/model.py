from datetime import datetime
from typing import Self
from pydantic import model_validator
from api.back.decore import BaseMessage
from libs.model.exp import BaseModelWithRawArray
from libs.dt.utils import pretty_str

class SourceMessage(BaseMessage):
    pass

class SourceSignal(BaseModelWithRawArray):
    title: str
    created: datetime

class SourceSignalKV(BaseModelWithRawArray):
    id: int
    title: str

class SourceSelector(BaseModelWithRawArray):
    id: int
    created: datetime | str
    title: str

    @model_validator(mode='after')
    def complete(self) -> Self:
        if isinstance(self.created, datetime):
            self.created = pretty_str(self.created)
        return self
