import logging
from api.back.cards.model import CardSignal, CardsMessage
from money.models import Cards

logger = logging.getLogger(__name__)

def add_cards_data(item: CardsMessage) -> dict:
    elem = Cards.objects.create(title=item.title, amount=item.amount, number=item.number, user_id=item.user_id)
    elem.created = item.created
    elem.save()
    return dict(data='ok', message=f'adding Shop key: {elem.pk}')

def delete_cards_row(item: CardsMessage) -> dict:
    Cards.objects.filter(pk=item.pk).delete()
    return dict(data='ok', message=f'delete Shop key: {item.pk}')

def get_cards_row(item: CardsMessage) -> dict:
    data: dict = {}
    for it in Cards.objects.filter(pk=item.pk):
        data = CardSignal.from_orm(it).model_dump()
    return data

def edit_cards_data(item: CardsMessage) -> dict:
    try:
        elem = Cards.objects.get(pk=item.pk)

        elem.title = item.title
        elem.amount = item.amount
        elem.number = item.number
        elem.created = item.created
        elem.save()
    except: # noqa
        return dict(data='err', message='pk does not exist')

    return dict(data='ok', message=f'update {item.pk=}')
