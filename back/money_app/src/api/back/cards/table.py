import logging
from api.back.decore import draw_paginate
from api.back.cards.model import CardSelector, CardsMessage
from money.models import Cards
from api.back.cards.query import SQL_CARDS, CARDS_TOTAL

logger = logging.getLogger(__name__)

@draw_paginate  # type: ignore
def table_cards_data(item: CardsMessage) -> tuple:
    params = [item.user_id, item.offset * item.limit, item.limit]
    ls = [CardSelector.from_orm(it).model_dump() for it in Cards.objects.raw(raw_query=SQL_CARDS, params=params)]

    params = [item.user_id]
    count: int = 0
    for it in Cards.objects.raw(raw_query=CARDS_TOTAL, params=params):
        count = it.c

    return ls, count, item.offset, item.limit
