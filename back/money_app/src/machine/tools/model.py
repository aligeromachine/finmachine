from datetime import datetime
from decimal import Decimal
from libs.dt.utils import pretty_str
from libs.model.exp import BaseModelWithRawArray
from typing import Self
from pydantic import Field, model_validator
from libs.validate.exp import validate_list_conv

class Payload(BaseModelWithRawArray):
    dt: int
    buy: float
    profit: float

class WidgetRange(BaseModelWithRawArray):
    dt: int
    buy: Decimal = Decimal(0)
    profit: Decimal = Decimal(0)

class FinStat(BaseModelWithRawArray):
    payload: list[WidgetRange] | str
    user_id: int

    @model_validator(mode='after')
    def complete(self) -> Self:
        if isinstance(self.payload, str):
            self.payload = validate_list_conv(self.payload, WidgetRange)
        return self

class WidgetDaily(BaseModelWithRawArray):
    title: datetime | str = Field(..., alias='dt')
    amount: Decimal = Decimal(0)

    @model_validator(mode='after')
    def complete(self) -> Self:
        if isinstance(self.title, datetime):
            self.title = pretty_str(self.title).strip('00:00:00')
        return self
    

class WidgetShop(BaseModelWithRawArray):
    title: str
    amount: Decimal = Decimal(0)
