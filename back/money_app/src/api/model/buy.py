from api.model.main import ExtModel
from decimal import Decimal

class BuyMessage(ExtModel):
    amount: Decimal = 0
    shop: int = 0
    prod: int = 0
