from datetime import datetime
from decimal import Decimal
from api.back.model import AmountSelector, AmountSignal, BaseMessage

class BuyMessage(BaseMessage):
    amount: Decimal = Decimal(0)
    shop: int = 0
    prod: int = 0

class BuySignal(AmountSignal):
    shop: int
    cat: int
    prod: int
    created: datetime

class BuySelector(AmountSelector):
    shop: str
    cat: str
    prod: str
