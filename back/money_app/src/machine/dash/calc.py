from datetime import datetime
from typing import Self, TypeVar
from pydantic import BaseModel, model_validator
from decimal import Decimal
from machine.tools.selector import get_list_user_finance, get_top_user_cards, get_user_date_range, get_user_total_amount
from machine.dash.model import Capital, CardsAgg, DateRng, Rng
from machine.tools.model import WidgetRange
from functools import reduce

T = TypeVar('T', bound='ReduceInfo')

class ReduceInfo(BaseModel):
    calcWgRange: list[WidgetRange] = []
    calcWgYears: list[WidgetRange] = []
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
        raw: dict = dict(
            calcWgRange=get_user_date_range(user_id=user_id),
            calcWgYears=get_list_user_finance(user_id=user_id), 
            totalSumCards=get_user_total_amount(user_id=user_id), 
            cards=get_top_user_cards(user_id=user_id)
        )
        return cls(**raw)
