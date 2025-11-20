from decimal import Decimal
from money.models import Buy


def get_buy_amount_by_id(pk: int) -> Decimal:
    buy = Buy.objects.get(pk=pk)
    return Decimal(buy.amount)
