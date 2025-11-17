from decimal import Decimal
from machine.tools.query import SQL_ORDER_CARDS, SQL_WIDGET_RANGE
from machine.tools.model import WidgetRange
from money.libs.validate.exp import validate_list
from money.models import AuditFin, Cards
from machine.dash.model import CardSelector, CardsAgg
from django.db.models import Sum

def get_list_user_finance(user_id: int) -> list[WidgetRange]:
    finance_years: list[WidgetRange] = []
    for it in AuditFin.objects.filter(user_id=user_id):
        finance_years = validate_list(it.payload, WidgetRange, prn=True)

    return finance_years

def get_top_user_cards(user_id: int) -> CardsAgg:
    cards: CardsAgg = CardsAgg()
    params = [user_id]    
    for index, it in enumerate(Cards.objects.raw(raw_query=SQL_ORDER_CARDS, params=params)):
        if index == 0:
            cards.one = CardSelector.from_orm(it)
        if index == 1:
            cards.two = CardSelector.from_orm(it)
        if index == 2:
            cards.three = CardSelector.from_orm(it)

    return cards

def get_user_total_amount(user_id: int) -> Decimal:
    total: Decimal = Cards.objects.filter(user_id=user_id).aggregate(total=Sum('amount'))['total'] or Decimal(0)
    return total

def get_user_date_range(user_id: int) -> list[WidgetRange]:
    params = [user_id] * 6
    finance_rng: list[WidgetRange] = [WidgetRange.from_orm(it) for it in AuditFin.objects.raw(raw_query=SQL_WIDGET_RANGE, params=params)]
    return finance_rng
