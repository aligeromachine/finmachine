from api.model.main import ExtModel
from decimal import Decimal

class CardsMessage(ExtModel):
    number: str = ''
    amount: Decimal = 0
