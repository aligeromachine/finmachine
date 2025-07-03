import logging
from api.back.buy.model import BuyMessage, BuySignal
from money.utils.func import model_max_id
from money.models import Buy
from api.back.buy.query import BUY_ROW

logger = logging.getLogger(__name__)

def add_buy_data(item: BuyMessage) -> dict:
    Buy(
        title=item.title,
        amount=item.amount,
        shop_id=item.shop,
        products_id=item.prod,
        user_id=item.user_id
    ).save()
    max_id = model_max_id(model=Buy)

    return {'data': 'ok', 'message': f'adding Buy key: {max_id}'}

def delete_buy_row(item: BuyMessage):
    Buy.objects.filter(pk=item.pk).delete()
    return {'data': 'ok', 'message': f'delete Buy key: {item.pk}'}

def get_buy_row(item: BuyMessage):
    data = {}
    for it in Buy.objects.raw(raw_query=BUY_ROW, params=[item.pk]):
        data = BuySignal.from_orm(it).model_dump()
    return data

def edit_buy_data(item: BuyMessage):
    try:
        instance = Buy.objects.get(pk=item.pk)

        instance.title = item.title
        instance.amount = item.amount
        instance.shop_id = item.shop
        instance.products_id = item.prod
        instance.save()
    except: # noqa
        return {'data': 'err', 'message': 'pk does not exist'}

    return {'data': 'ok', 'message': f'update {item.pk=}'}
