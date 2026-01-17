from datetime import datetime, timedelta
from decimal import Decimal
import logging
from typing import Self
from pydantic import BaseModel, model_validator
from libs.math.exp import trim_decimal
from libs.model.exp import BaseModelWithRawArray
from libs.dt.utils import pretty_str, time_parse
from libs.const import CONST

logger = logging.getLogger(__name__)

class MainModel(BaseModel):
    user_id: int = 0
    command: str

class FData(BaseModel):
    b64: str
    name: str
    type: str

class BaseMessage(MainModel):
    offset: int = 0
    limit: int = 0
    pk: int = 0
    title: str = ''
    created: str | datetime = datetime.now() + timedelta(hours=3)

    @model_validator(mode='after')
    def base_message(self) -> Self:
        if isinstance(self.created, str) and self.created:
            dt: datetime | None = time_parse(raw=self.created)
            if not dt:
                raise Exception(f"{self.created} does not match with {CONST.FormatFull}, {CONST.FormatJS}")

            self.created = dt
        return self

class AmountSignal(BaseModelWithRawArray):
    title: str
    amount: Decimal

    @model_validator(mode='after')
    def amount_signal(self) -> Self:
        self.amount = trim_decimal(self.amount)
        return self
    
class BaseSelector(BaseModelWithRawArray):
    id: int
    created: datetime | str
    title: str

    @model_validator(mode='after')
    def base_selector(self) -> Self:
        if isinstance(self.created, datetime):
            self.created = pretty_str(self.created)
        return self

class AmountSelector(BaseSelector):
    amount: Decimal

    @model_validator(mode='after')
    def amount_selector(self) -> Self:
        self.amount = trim_decimal(self.amount)
        return self
