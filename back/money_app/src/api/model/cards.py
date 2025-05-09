from api.model.main import MainModel
from decimal import Decimal

class CardsMessage(MainModel):
    pk: int = 0
    offset: int = 0
    limit: int = 0
    title: str = ''
    number: str = ''
    amount: Decimal = 0
