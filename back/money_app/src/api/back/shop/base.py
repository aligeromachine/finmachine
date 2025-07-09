import logging
from api.back.shop.model import ShopMessage, ShopSignal, ShopSignalKV
from money.models import Shop

logger = logging.getLogger(__name__)

def add_shop_data(item: ShopMessage) -> dict:
    elem = Shop.objects.create(title=item.title, address=item.address, user_id=item.user_id)
    elem.created = item.created
    elem.save()
    return {'data': 'ok', 'message': f'adding shop key: {elem.pk}'}

def delete_shop_row(item: ShopMessage) -> dict:
    Shop.objects.filter(pk=item.pk).delete()
    return {'data': 'ok', 'message': f'delete shop key: {item.pk}'}

def get_shop_row(item: ShopMessage) -> dict:
    data: dict = {}
    for it in Shop.objects.filter(pk=item.pk):
        data = ShopSignal.from_orm(it).model_dump()
    return data

def edit_shop_data(item: ShopMessage) -> dict:
    try:
        elem = Shop.objects.get(pk=item.pk)

        elem.title = item.title
        elem.address = item.address
        elem.created = item.created
        elem.save()
    except: # noqa
        return {'data': 'err', 'message': 'pk does not exist'}

    return {'data': 'ok', 'message': f'update {item.pk=}'}

def list_shop_data(item: ShopMessage) -> list:
    ls: list = [ShopSignalKV(id=it.pk, title=f"{it.title} - {it.address}").model_dump() for it in Shop.objects.filter(user=item.user_id)]
    return ls
