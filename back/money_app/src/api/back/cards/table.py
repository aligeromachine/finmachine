import logging
from src.libs.django.base import count_raw_sql
from libs.decore.utils import draw_paginate
from api.back.cards.model import CardSelector, CardsMessage
from money.models import Cards
from api.back.cards.query import SQL_CARDS, CARDS_TOTAL

logger = logging.getLogger(__name__)

@draw_paginate  # type: ignore
def table_cards_data(item: CardsMessage) -> tuple:
    params = [item.user_id, item.offset * item.limit, item.limit]
    ls = [CardSelector.from_orm(it).model_dump() for it in Cards.objects.raw(raw_query=SQL_CARDS, params=params)]
    count: int = count_raw_sql(model=Cards, sql=CARDS_TOTAL, params=[item.user_id])

    return ls, count, item.offset, item.limit
