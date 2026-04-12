from decimal import Decimal
from typing import Self
from pydantic import BaseModel, model_validator
from libs.math.exp import trim_decimal
from libs.model.exp import BaseModelWithRawArray

class Rng():
    WEEK: int = 1
    MONTH: int = 2
    DAY: int = 3

class DateRng(BaseModel):
    year: Decimal = Decimal(0)
    month: Decimal = Decimal(0)
    week: Decimal = Decimal(0)
    day: Decimal = Decimal(0)

    @model_validator(mode='after')
    def complete(self) -> Self:
        self.year = trim_decimal(self.year)
        self.month = trim_decimal(self.month)
        self.week = trim_decimal(self.week)
        self.day = trim_decimal(self.day)
        return self

class Capital(BaseModel):
    cash: Decimal = Decimal(0)
    cards: Decimal = Decimal(0)
    year: Decimal = Decimal(0)

    @model_validator(mode='after')
    def complete(self) -> Self:
        self.cash = trim_decimal(self.cash)
        self.cards = trim_decimal(self.cards)
        self.year = trim_decimal(self.year)
        return self

class CardSelector(BaseModelWithRawArray):
    title: str = ""
    amount: Decimal = Decimal(0)

    @model_validator(mode='after')
    def complete(self) -> Self:
        self.amount = trim_decimal(self.amount)
        return self

class CardsAgg(BaseModel):
    one: CardSelector = CardSelector()
    two: CardSelector = CardSelector()
    three: CardSelector = CardSelector()

class TopTitle(BaseModel):
    title: str
    amount: Decimal = Decimal(0)

    @model_validator(mode='after')
    def complete(self) -> Self:
        self.amount = trim_decimal(self.amount)
        return self
