from decimal import Decimal
from pydantic import BaseModel
from money.libs.model.exp import BaseModelWithRawArray

class Rng():
    WEEK: int = 1
    MONTH: int = 2
    DAY: int = 3

class DateRng(BaseModel):
    year: Decimal = Decimal(0)
    month: Decimal = Decimal(0)
    week: Decimal = Decimal(0)
    day: Decimal = Decimal(0)

class Capital(BaseModel):
    cash: Decimal = Decimal(0)
    cards: Decimal = Decimal(0)
    year: Decimal = Decimal(0)

class CardSelector(BaseModelWithRawArray):
    title: str = ""
    amount: Decimal = Decimal(0)

class CardsAgg(BaseModel):
    one: CardSelector = CardSelector()
    two: CardSelector = CardSelector()
    three: CardSelector = CardSelector()
