from datetime import datetime
from typing import Self
from pydantic import Field, model_validator
from decimal import Decimal
from api.back.model import AmountSelector, BaseMessage
from libs.math.exp import trim_decimal
from libs.model.exp import BaseModelWithRawArray

class ProfitMessage(BaseMessage):
    amount: Decimal = Decimal(0)
    source: int = 0

class ProfitSignal(BaseModelWithRawArray):
    title: str
    amount: Decimal
    source: int = Field(..., alias="source_id")
    created: datetime

    @model_validator(mode='after')
    def complete(self) -> Self:
        self.amount = trim_decimal(self.amount)
        return self

class ProfitSelector(AmountSelector):
    source: str
