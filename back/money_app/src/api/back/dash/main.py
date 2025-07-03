from api.model.dash import DashboardMessage
from django.http import HttpRequest
import logging
from django.contrib.auth.models import User
from api.back.dash.etl import (
    elt_trati, etl_prih, etl_prih_vid, etl_prod, etl_prod_vid, etl_shop, etl_visa)
from api.model.main import validate_model
from api.back.dash.upt import update_products, update_profit, update_buy

logger = logging.getLogger(__name__)

def update_money_csv(item: DashboardMessage) -> dict:
    respo = {"data": "ok", "message": "update_money_csv"}

    def GetAddressWatchService():
        user = User.objects.get(pk=1)
        logger.info('ETL')
        etl_shop(user=user)
        etl_prih_vid(user=user)
        etl_prih(user=user)
        etl_prod_vid(user=user)
        etl_prod(user=user)
        etl_visa(user=user)
        elt_trati(user=user)

        logger.info('update_products')
        update_products()
        logger.info('update_profit')
        update_profit()
        logger.info('update_buy')
        update_buy()
        logger.info('END')

    import threading
    threading.Thread(target=GetAddressWatchService, args=()).start()

    return respo

@validate_model(DashboardMessage)
def invoke_response(request: HttpRequest, item: DashboardMessage) -> dict:
    respo = {"data": "err", "message": "undefinded"}

    if item.command == "update_money_csv":
        respo = update_money_csv(item=item)

    return respo
