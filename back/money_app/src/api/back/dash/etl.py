from datetime import datetime
from decimal import Decimal
import logging
from money.libs.ext_c import CONST
from django.contrib.auth.models import User
from money.libs.ext_utils import reder_csv
from api.model.etl_acccess import Prod, Trati, Organiz, Prihvid, Prih, Prodvid, Visa
from money.models import Buy, Cards, Products, Shop, Source, Profit, Catalog
from money.utils.func import get_raw_path, model_max_id
from django.db import models

logger = logging.getLogger(__name__)

def conv_dt(cdt: str):
    return datetime.strptime(cdt, CONST.FormatAccess)

def update_created(cdt: str, model:  models.Model):
    pk: int = model_max_id(model=model)
    dt: datetime = conv_dt(cdt=cdt)

    model.objects.filter(pk=pk).update(created=dt)

def extract(nfile: str, model: any):
    rfile = f'{get_raw_path()}/{nfile}.csv'
    elastic_data = [model(*it) for it in reder_csv(rfile)]
    logger.info(f'{str(model)}: {len(elastic_data)}')
    return elastic_data

# Organiz -> Shop
def etl_shop(user: User):
    for chunk in extract(nfile='org', model=Organiz):
        Shop(
            title=chunk.name_org,
            address=chunk.adress_org,
            state_id=chunk.kod_org,
            user=user
        ).save()

# Prihvid -> Source
def etl_prih_vid(user: User):
    for chunk in extract(nfile='prih_vid', model=Prihvid):
        Source(
            title=chunk.name_prih_vid,
            state_id=chunk.kod_prih_vid,
            user=user
        ).save()

# Prih -> Profit
def etl_prih(user: User):
    for chunk in extract(nfile='prih', model=Prih):
        amount = Decimal(chunk.sum_prih)
        Profit(
            title=chunk.prim_prih,
            source_id=chunk.kod_prih_vid_v,
            state_id=chunk.kod_prih,
            amount=amount,
            user=user
        ).save()

        update_created(cdt=chunk.data_prih, model=Profit)

# Prodvid -> Catalog
def etl_prod_vid(user: User):
    for chunk in extract(nfile='prod_vid', model=Prodvid):
        Catalog(
            title=chunk.name_prod_vid,
            state_id=chunk.kod_prod_vid,
            user=user
        ).save()

# Prod -> Products
def etl_prod(user: User):
    for chunk in extract(nfile='prod', model=Prod):
        Products(
            title=chunk.name_prod,
            state_id=chunk.kod_prod,
            catalog_id=chunk.kod_prod_vid_v,
            user=user
        ).save()

# Visa -> Cards
def etl_visa(user: User):
    for chunk in extract(nfile='visa', model=Visa):
        amount = Decimal(chunk.visa_s)
        Cards(
            title=chunk.visa_n,
            state_id=chunk.id_visa,
            number=chunk.visa_nom,
            amount=amount,
            user=user
        ).save()

# Trati -> Buy
def elt_trati(user: User):
    for chunk in extract(nfile='trati', model=Trati):
        amount = Decimal(chunk.cena_tr)
        Buy(
            title=chunk.prim_tr,
            amount=amount,
            shop_id=chunk.kod_org_tr,
            products_id=chunk.kod_prod_tr,
            state_id=chunk.kod_pokup,
            user=user
        ).save()

        update_created(cdt=chunk.data_tr, model=Buy)
