from typing import Self
from pydantic import model_validator
from money.libs.validate import validate_list_conv
from money.libs.model import BaseModelWithRawArray

class Payload(BaseModelWithRawArray):
    year: int
    buy: float | None = None
    profit: float | None = None

class FinStat(BaseModelWithRawArray):
    payload: list[Payload] | str
    user_id: int

    @model_validator(mode='after')
    def complete(self) -> Self:
        if isinstance(self.payload, str):
            self.payload = validate_list_conv(self.payload, Payload)
        return self
