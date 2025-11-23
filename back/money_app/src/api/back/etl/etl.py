from datetime import datetime
from decimal import Decimal
import logging
from typing import Any
from money.libs.django.func import get_raw_path
from money.libs.files.exp import read_file_csv_list
from money.libs.const import CONST
from django.contrib.auth.models import User
from api.back.etl.model import Prod, Trati, Organiz, Prihvid, Prih, Prodvid, Visa
from money.models import Buy, Cards, Products, Shop, Source, Profit, Catalog

logger = logging.getLogger(__name__)

def conv_dt(cdt: str) -> datetime:
    return datetime.strptime(cdt, CONST.FormatAccess)

def extract(nfile: str, model: Any) -> list:
    rfile = f'{get_raw_path()}/{nfile}.csv'
    elastic_data = [model(*it) for it in read_file_csv_list(rfile)]
    logger.info(f'{str(model)}: {len(elastic_data)}')
    return elastic_data

# Organiz -> Shop
def etl_shop(user: User) -> None:
    for chunk in extract(nfile='org', model=Organiz):
        Shop(
            title=chunk.name_org,
            address=chunk.adress_org,
            state_id=chunk.kod_org,
            user=user
        ).save()

# Prihvid -> Source
def etl_prih_vid(user: User) -> None:
    for chunk in extract(nfile='prih_vid', model=Prihvid):
        Source(
            title=chunk.name_prih_vid,
            state_id=chunk.kod_prih_vid,
            user=user
        ).save()

# Prih -> Profit
def etl_prih(user: User) -> None:
    for chunk in extract(nfile='prih', model=Prih):
        amount = Decimal(chunk.sum_prih)
        p = Profit(
            title=chunk.prim_prih,
            source_id=chunk.kod_prih_vid_v,
            state_id=chunk.kod_prih,
            amount=amount,
            user=user
        )
        p.save()
        p.created = conv_dt(cdt=chunk.data_prih)
        p.save()

# Prodvid -> Catalog
def etl_prod_vid(user: User) -> None:
    for chunk in extract(nfile='prod_vid', model=Prodvid):
        Catalog(
            title=chunk.name_prod_vid,
            state_id=chunk.kod_prod_vid,
            user=user
        ).save()

# Prod -> Products
def etl_prod(user: User) -> None:
    for chunk in extract(nfile='prod', model=Prod):
        Products(
            title=chunk.name_prod,
            state_id=chunk.kod_prod,
            catalog_id=chunk.kod_prod_vid_v,
            user=user
        ).save()

# Visa -> Cards
def etl_visa(user: User) -> None:
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
def elt_trati(user: User) -> None:
    for chunk in extract(nfile='trati', model=Trati):
        amount = Decimal(chunk.cena_tr)
        p = Buy(
            title=chunk.prim_tr,
            amount=amount,
            shop_id=chunk.kod_org_tr,
            products_id=chunk.kod_prod_tr,
            state_id=chunk.kod_pokup,
            user=user
        )
        p.save()
        p.created = conv_dt(cdt=chunk.data_tr)
        p.save()
