from datetime import datetime
from django.db.models import Sum
from typing import Self, TypeVar
from pydantic import BaseModel, model_validator
from decimal import Decimal
from machine.func.model.sub import Capital, CardSelector, CardsAgg, DateRng, Rng
from machine.func.model.selector import WidgetYear, WidgetRange
from machine.func.query import SQL_ORDER_CARDS, SQL_WIDGET_RANGE
from money.libs.validate.exp import validate_list
from money.models import AuditFin, Cards
from functools import reduce

T = TypeVar('T', bound='ReduceInfo')

class ReduceInfo(BaseModel):
    calcWgRange: list[WidgetRange] = []
    calcWgYears: list[WidgetYear] = []
    totalSumCards: Decimal = Decimal(0)

    capital: Capital = Capital()
    cards: CardsAgg = CardsAgg()
    profit: DateRng = DateRng()
    buy: DateRng = DateRng()

    @model_validator(mode='after')
    def complete(self) -> Self:

        self.capital.cards = self.totalSumCards

        self.profit.month = reduce(lambda x, y: x + y, [it.profit for it in self.calcWgRange if it.dt == Rng.MONTH], Decimal(0))
        self.buy.month = reduce(lambda x, y: x + y, [it.buy for it in self.calcWgRange if it.dt == Rng.MONTH], Decimal(0))

        self.profit.week = reduce(lambda x, y: x + y, [it.profit for it in self.calcWgRange if it.dt == Rng.WEEK], Decimal(0))
        self.buy.week = reduce(lambda x, y: x + y, [it.buy for it in self.calcWgRange if it.dt == Rng.WEEK], Decimal(0))

        self.profit.day = reduce(lambda x, y: x + y, [it.profit for it in self.calcWgRange if it.dt == Rng.DAY], Decimal(0))
        self.buy.day = reduce(lambda x, y: x + y, [it.buy for it in self.calcWgRange if it.dt == Rng.DAY], Decimal(0))

        self.profit.year = reduce(lambda x, y: x + y, [it.profit for it in self.calcWgYears if it.dt == datetime.now().year], Decimal(0))
        self.buy.year = reduce(lambda x, y: x + y, [it.buy for it in self.calcWgYears if it.dt == datetime.now().year], Decimal(0))

        self.capital.year = self.profit.year - self.buy.year
        self.capital.cash = \
            reduce(lambda x, y: x + y, [it.profit for it in self.calcWgYears], Decimal(0)) - \
            reduce(lambda x, y: x + y, [it.buy for it in self.calcWgYears], Decimal(0)) - \
            self.capital.cards

        return self

    @classmethod
    def load_from_db(cls: type[T], user_id: int) -> T:
        wgYears: list[WidgetYear] = []
        for it in AuditFin.objects.filter(user_id=user_id):
            wgYears = validate_list(it.payload, WidgetYear, prn=True)

        cards: CardsAgg = CardsAgg()
        for index, it in enumerate(Cards.objects.raw(raw_query=SQL_ORDER_CARDS)):
            if index == 0:
                cards.one = CardSelector.from_orm(it)
            if index == 1:
                cards.two = CardSelector.from_orm(it)
            if index == 2:
                cards.three = CardSelector.from_orm(it)

        params = [user_id] * 6
        raw: dict = dict(
            calcWgRange=[WidgetRange.from_orm(it) for it in AuditFin.objects.raw(raw_query=SQL_WIDGET_RANGE, params=params)],
            calcWgYears=wgYears, 
            totalSumCards=Cards.objects.aggregate(total_amount=Sum('amount'))['total_amount'], 
            cards=cards
        )
        return cls(**raw)
