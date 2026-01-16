from datetime import datetime
from typing import Self
from libs.math.exp import trim_decimal
from libs.dt.utils import pretty_str
from pydantic import model_validator
from api.back.decore import BaseMessage
from decimal import Decimal
from libs.model.exp import BaseModelWithRawArray

class CardsMessage(BaseMessage):
    number: str = ''
    amount: Decimal = Decimal(0)

    @model_validator(mode='after')
    def complete(self) -> Self:
        self.amount = trim_decimal(self.amount)
        return self

class CardSignal(BaseModelWithRawArray):
    title: str
    amount: Decimal
    number: str
    created: datetime

    @model_validator(mode='after')
    def complete(self) -> Self:
        self.amount = trim_decimal(self.amount)
        return self

class CardSelector(BaseModelWithRawArray):
    id: int
    created: datetime | str
    title: str
    amount: Decimal
    number: str

    @model_validator(mode='after')
    def complete(self) -> Self:
        if isinstance(self.created, datetime):
            self.created = pretty_str(self.created)
        self.amount = trim_decimal(self.amount)
        return self
