from datetime import datetime
from typing import Self
from money.libs.ext_utils import dateDRF
from pydantic import model_validator
from api.model.main import ExtModel
from decimal import Decimal
from money.libs.model import BaseModelWithRawArray

class CardsMessage(ExtModel):
    number: str = ''
    amount: Decimal = 0

class CardSignal(BaseModelWithRawArray):
    title: str
    amount: Decimal
    number: int

class CardSelector(BaseModelWithRawArray):
    id: int
    created: datetime | str
    title: str
    amount: Decimal
    number: str

    @model_validator(mode='after')
    def complete(self) -> Self:
        if isinstance(self.created, datetime):
            self.created = dateDRF(self.created)
        return self
