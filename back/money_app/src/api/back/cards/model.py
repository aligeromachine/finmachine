from datetime import datetime
from typing import Self
from api.back.model import AmountSelector, AmountSignal, BaseMessage
from libs.math.exp import trim_decimal
from pydantic import model_validator
from decimal import Decimal

class CardsMessage(BaseMessage):
    number: str = ''
    amount: Decimal = Decimal(0)

    @model_validator(mode='after')
    def cards_message(self) -> Self:
        self.amount = trim_decimal(self.amount)
        return self

class CardSignal(AmountSignal):
    number: str
    created: datetime

class CardSelector(AmountSelector):
    number: str
