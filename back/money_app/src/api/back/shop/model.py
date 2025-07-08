from datetime import datetime, timedelta
import logging
import re
from typing import Self
from pydantic import model_validator
from api.back.decore import ExtModel
from money.libs.model import BaseModelWithRawArray
from money.libs.ext_utils import dateDRF

logger = logging.getLogger(__name__)

class ShopMessage(ExtModel):
    address: str = ''
    created: datetime | str = datetime.now() + timedelta(hours=3)

    @model_validator(mode='after')
    def complete(self) -> Self:
        if isinstance(self.created, str) and self.created:
            self.created = datetime.strptime(self.created, "%a %b %d %Y %H:%M:%S")
        return self

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
