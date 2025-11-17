from api.back.decore import MainModel
from dataclasses import dataclass
from machine.dash.model import Capital, CardsAgg, DateRng
from money.libs.model.exp import BaseModelWithRawArray
import logging

logger = logging.getLogger(__name__)

class DashboardMessage(MainModel):
    pass

class DashSignal(BaseModelWithRawArray):
    capital: Capital = Capital()
    cards: CardsAgg = CardsAgg()
    profit: DateRng = DateRng()
    buy: DateRng = DateRng()

    def to_dash(self) -> dict:
        data: dict = dict(
            capital=self.capital.model_dump(),
            cards=self.cards.model_dump(),
            profit=self.profit.model_dump(),
            buy=self.buy.model_dump(),
        )
        return data

@dataclass
class Organiz:
    kod_org: int
    name_org: str
    adress_org: str

@dataclass
class Prihvid:
    kod_prih_vid: int
    name_prih_vid: str

@dataclass
class Prih:
    kod_prih: int
    kod_prih_vid_v: int
    sum_prih: str
    data_prih: str
    prim_prih: str

@dataclass
class Prodvid:
    kod_prod_vid: int
    name_prod_vid: str

@dataclass
class Prod:
    kod_prod: int
    kod_prod_vid_v: int
    name_prod: str

@dataclass
class Visa:
    id_visa: int
    visa_n: str
    visa_nom: str
    visa_s: str

@dataclass
class Trati:
    kod_pokup: int
    kod_prod_tr: int
    kod_org_tr: int
    cena_tr: str
    kol_ed_tr: str
    data_tr: str
    prim_tr: str

    def __post_init__(self) -> None:
        self.prim_tr = f'{self.prim_tr} {self.kol_ed_tr}'
