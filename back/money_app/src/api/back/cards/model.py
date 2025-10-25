from datetime import datetime
from typing import Self
from money.libs.dt.utils import pretty_str
from pydantic import model_validator
from api.back.decore import ExtModel
from decimal import Decimal
from money.libs.model.exp import BaseModelWithRawArray

class CardsMessage(ExtModel):
    number: str = ''
    amount: Decimal = Decimal(0)

class CardSignal(BaseModelWithRawArray):
    title: str
    amount: Decimal
    number: str
    created: datetime

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
        return self
