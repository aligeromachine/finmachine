from datetime import datetime
from django.db.models import Sum
from typing import Self, TypeVar
from pydantic import BaseModel, model_validator
from decimal import Decimal
from machine.func.query import SQL_TOTAL_WEEK_MONTH
from money.libs.validate import validate_list
from money.models import AuditFin, Cards
from money.libs.model import BaseModelWithRawArray
from functools import reduce

T = TypeVar('T', bound='ReduceInfo')

WEEK: int = 1
MONTH: int = 2

class PayloadSelector(BaseModelWithRawArray):
    year: int
    buy: Decimal
    profit: Decimal

class WM(BaseModelWithRawArray):
    raw: int
    buy: Decimal
    profit: Decimal

class ReduceInfo(BaseModel):
    money_cash: Decimal = Decimal(0)

    profit_sum: Decimal = Decimal(0)
    profit_year: Decimal = Decimal(0)
    profit_month: Decimal = Decimal(0)
    profit_week: Decimal = Decimal(0)

    buy_sum: Decimal = Decimal(0)
    buy_year: Decimal = Decimal(0)
    buy_month: Decimal = Decimal(0)
    buy_week: Decimal = Decimal(0)

    card_sum: Decimal = Decimal(0)

    payload: list[PayloadSelector] = []
    wm: list[WM] = []

    @model_validator(mode='after')
    def complete(self) -> Self:
        self.profit_sum = reduce(lambda x, y: x + y, [it.profit for it in self.payload], Decimal(0))
        self.buy_sum = reduce(lambda x, y: x + y, [it.buy for it in self.payload], Decimal(0))

        self.money_cash = self.profit_sum - self.buy_sum - self.card_sum

        self.profit_year = reduce(lambda x, y: x + y, [it.profit for it in self.payload if it.year == datetime.now().year], Decimal(0))
        self.buy_year = reduce(lambda x, y: x + y, [it.buy for it in self.payload if it.year == datetime.now().year], Decimal(0))

        self.profit_month = reduce(lambda x, y: x + y, [it.profit for it in self.wm if it.raw == MONTH], Decimal(0))
        self.buy_month = reduce(lambda x, y: x + y, [it.buy for it in self.wm if it.raw == MONTH], Decimal(0))

        self.profit_week = reduce(lambda x, y: x + y, [it.profit for it in self.wm if it.raw == WEEK], Decimal(0))
        self.buy_week = reduce(lambda x, y: x + y, [it.buy for it in self.wm if it.raw == WEEK], Decimal(0))

        return self

    @classmethod
    def load_from_db(cls: type[T], user_id: int) -> T:
        payload: list[PayloadSelector] = []
        for it in AuditFin.objects.filter(user_id=user_id):
            payload = validate_list(it.payload, PayloadSelector, prn=True)

        card_sum: Decimal = Cards.objects.aggregate(total_amount=Sum('amount'))['total_amount']

        params = [user_id] * 4
        wm: list[WM] = [WM.from_orm(it) for it in AuditFin.objects.raw(raw_query=SQL_TOTAL_WEEK_MONTH, params=params)]

        raw: dict = dict(payload=payload, card_sum=card_sum, wm=wm)
        return cls(**raw)

    # @classmethod
    # def get_selector(cls, machine: str) -> list[str]:
    #     raw_speed: list[SpeedMacSelector] = cls.get_speed()

    #     selector: list[str] = []

    #     for it in raw_speed:
    #         if machine == it.machine:
    #             selector.extend(it.hashtypes)

    #     selector = sorted(selector, key=lambda x: int(x))

    #     return selector
