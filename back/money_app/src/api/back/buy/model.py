from datetime import datetime
from typing import Self
from api.back.decore import ExtModel
from decimal import Decimal
from pydantic import model_validator
from money.libs.model import BaseModelWithRawArray
from money.libs.ext_utils import dateDRF

class BuyMessage(ExtModel):
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

class BuySelector(BaseModelWithRawArray):
    id: int
    created: datetime | str
    title: str
    amount: Decimal
    shop: str
    cat: str
    prod: str

    @model_validator(mode='after')
    def complete(self) -> Self:
        if isinstance(self.created, datetime):
            self.created = dateDRF(self.created)
        return self
