from decimal import Decimal
from pydantic import BaseModel, Field
from api.back.decore import MainModel
from dataclasses import dataclass
from money.libs.model import BaseModelWithRawArray
import logging

logger = logging.getLogger(__name__)

class DashboardMessage(MainModel):
    pass

class ProfitSignal(BaseModel):
    year: Decimal = Field(..., alias="profit_year")
    month: Decimal = Field(..., alias="profit_month")
    week: Decimal = Field(..., alias="profit_week")
    day: Decimal = Field(..., alias="profit_day")

class BuySignal(BaseModel):
    year: Decimal = Field(..., alias="buy_year")
    month: Decimal = Field(..., alias="buy_month")
    week: Decimal = Field(..., alias="buy_week")
    day: Decimal = Field(..., alias="buy_day")

class CashSignal(BaseModel):
    card_sum: Decimal
    capital_year: Decimal
    money_cash: Decimal

class CardSignal(BaseModel):
    one_name: str = Field(..., alias="card_one_name")
    one_sum: Decimal = Field(..., alias="card_one_sum")
    two_name: str = Field(..., alias="card_two_name")
    two_sum: Decimal = Field(..., alias="card_two_sum")
    three_name: str = Field(..., alias="card_three_name")
    three_sum: Decimal = Field(..., alias="card_three_sum")

class DashSignal(BaseModelWithRawArray):
    profit_sum: Decimal
    profit_year: Decimal
    profit_month: Decimal
    profit_week: Decimal
    profit_day: Decimal

    buy_sum: Decimal
    buy_year: Decimal
    buy_month: Decimal
    buy_week: Decimal
    buy_day: Decimal

    card_sum: Decimal
    capital_year: Decimal
    money_cash: Decimal

    card_one_name: str
    card_one_sum: Decimal
    card_two_name: str
    card_two_sum: Decimal
    card_three_name: str
    card_three_sum: Decimal

    def to_dash(self) -> dict:
        raw = self.model_dump()
        data: dict = {
            "profit": ProfitSignal(**raw).model_dump(),
            "buy": BuySignal(**raw).model_dump(),
            "cash": CashSignal(**raw).model_dump(),
            "card": CardSignal(**raw).model_dump()
        }
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
