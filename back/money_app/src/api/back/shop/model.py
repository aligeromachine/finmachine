from datetime import datetime
import logging
from typing import Self
from pydantic import model_validator
from api.back.decore import ExtModel
from money.libs.model import BaseModelWithRawArray
from money.libs.ext_utils import dateDRF

logger = logging.getLogger(__name__)

class ShopMessage(ExtModel):
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
            self.created = dateDRF(self.created)
        return self
