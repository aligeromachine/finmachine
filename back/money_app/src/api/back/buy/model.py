from datetime import datetime
from typing import Self
from api.back.decore import BaseMessage, BaseSelector
from decimal import Decimal
from pydantic import model_validator
from libs.math.exp import trim_decimal
from libs.model.exp import BaseModelWithRawArray

class BuyMessage(BaseMessage):
    amount: Decimal = Decimal(0)
    shop: int = 0
    prod: int = 0

class BuySignal(BaseModelWithRawArray):
    title: str
    amount: Decimal
    shop: int
    cat: int
    prod: int
    created: datetime

    @model_validator(mode='after')
    def complete(self) -> Self:
        self.amount = trim_decimal(self.amount)
        return self

class BuySelector(BaseSelector):
    amount: Decimal
    shop: str
    cat: str
    prod: str

    @model_validator(mode='after')
    def complete(self) -> Self:
        self.amount = trim_decimal(self.amount)
        return self
