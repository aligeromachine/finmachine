import logging
from api.back.profit.model import ProfitMessage, ProfitSignal
from money.utils.func import model_max_id
from money.models import Profit
from api.back.profit.query import PROFIT_ROW

logger = logging.getLogger(__name__)

def add_profit_data(item: ProfitMessage) -> dict:
    Profit(
        title=item.title,
        amount=item.amount,
        source_id=item.source,
        user_id=item.user_id
    ).save()
    max_id = model_max_id(model=Profit)

    return {'data': 'ok', 'message': f'adding Profit key: {max_id}'}

def delete_profit_row(item: ProfitMessage) -> dict:
    Profit.objects.filter(pk=item.pk).delete()
    return {'data': 'ok', 'message': f'delete Profit key: {item.pk}'}

def get_profit_row(item: ProfitMessage) -> dict:
    data: dict = {}
    for it in Profit.objects.raw(raw_query=PROFIT_ROW, params=[item.pk]):
        data = ProfitSignal.from_orm(it).model_dump()
    return data

def edit_profit_data(item: ProfitMessage) -> dict:
    try:
        instance = Profit.objects.get(pk=item.pk)

        instance.title = item.title
        instance.amount = item.amount
        instance.source_id = item.source
        instance.save()
    except: # noqa
        return {'data': 'err', 'message': 'pk does not exist'}

    return {'data': 'ok', 'message': f'update {item.pk=}'}
