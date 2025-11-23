from decimal import Decimal
from money.models import Buy, Profit

def get_buy_amount_by_id(pk: int) -> Decimal:
    elem = Buy.objects.get(pk=pk)
    return Decimal(elem.amount)

def get_profit_amount_by_id(pk: int) -> Decimal:
    elem = Profit.objects.get(pk=pk)
    return Decimal(elem.amount)
