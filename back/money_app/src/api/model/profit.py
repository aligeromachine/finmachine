from api.model.main import ExtModel
from decimal import Decimal

class ProfitMessage(ExtModel):
    amount: Decimal = 0
    source: int = 0
