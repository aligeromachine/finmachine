from datetime import datetime
import logging
from typing import Self
from pydantic import model_validator
from api.back.decore import BaseMessage
from libs.model.exp import BaseModelWithRawArray
from libs.dt.utils import pretty_str

logger = logging.getLogger(__name__)

class ShopMessage(BaseMessage):
    address: str = ''

class ShopSignal(BaseModelWithRawArray):
    title: str
    address: str
    created: datetime

class ShopSignalKV(BaseModelWithRawArray):
    id: int
    title: str

class ShopSelector(BaseModelWithRawArray):
    id: int
    created: datetime | str
    title: str
    address: str

    @model_validator(mode='after')
    def complete(self) -> Self:
        if isinstance(self.created, datetime):
            self.created = pretty_str(self.created)
        return self
