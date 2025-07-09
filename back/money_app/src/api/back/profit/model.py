from datetime import datetime
from typing import Self
from pydantic import Field, model_validator
from api.back.decore import ExtModel
from decimal import Decimal
from money.libs.model import BaseModelWithRawArray
from money.libs.ext_utils import dateDRF

class ProfitMessage(ExtModel):
    amount: Decimal = Decimal(0)
    source: int = 0

class ProfitSignal(BaseModelWithRawArray):
    title: str
    amount: Decimal
    source: int = Field(..., alias="source_id")
    created: datetime

class ProfitSelector(BaseModelWithRawArray):
    id: int
    created: datetime | str
    title: str
    amount: Decimal
    source: str

    @model_validator(mode='after')
    def complete(self) -> Self:
        if isinstance(self.created, datetime):
            self.created = dateDRF(self.created)
        return self
