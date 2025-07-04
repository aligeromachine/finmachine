from datetime import datetime
from typing import Self
from pydantic import model_validator
from api.model.main import ExtModel
from decimal import Decimal
from money.libs.model import BaseModelWithRawArray
from money.libs.ext_utils import dateDRF

class ProfitMessage(ExtModel):
    amount: Decimal = 0
    source: int = 0

class ProfitSignal(BaseModelWithRawArray):
    title: str
    source: int

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
