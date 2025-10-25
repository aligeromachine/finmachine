from datetime import datetime
from typing import Self
from api.back.decore import ExtModel
from decimal import Decimal
from pydantic import model_validator
from money.libs.model.exp import BaseModelWithRawArray
from money.libs.dt.utils import pretty_str

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
            self.created = pretty_str(self.created)
        return self
