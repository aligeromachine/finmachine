from api.model.main import MainModel
from decimal import Decimal

class ProfitMessage(MainModel):
    pk: int = 0
    offset: int = 0
    limit: int = 0
    title: str = ''
    amount: Decimal = 0
    source: int = 0
