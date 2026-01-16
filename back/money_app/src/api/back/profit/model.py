from datetime import datetime
from typing import Self
from pydantic import Field, model_validator
from api.back.decore import BaseMessage
from decimal import Decimal
from libs.math.exp import trim_decimal
from libs.model.exp import BaseModelWithRawArray
from libs.dt.utils import pretty_str

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

class ProfitSelector(BaseModelWithRawArray):
    id: int
    created: datetime | str
    title: str
    amount: Decimal
    source: str

    @model_validator(mode='after')
    def complete(self) -> Self:
        if isinstance(self.created, datetime):
            self.created = pretty_str(self.created)
        self.amount = trim_decimal(self.amount)
        return self
