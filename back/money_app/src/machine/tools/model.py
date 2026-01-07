from decimal import Decimal
from libs.model.exp import BaseModelWithRawArray
from typing import Self
from pydantic import model_validator
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
