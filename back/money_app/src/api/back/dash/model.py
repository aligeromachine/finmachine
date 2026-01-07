from api.back.decore import MainModel
from machine.dash.model import Capital, CardsAgg, DateRng
from libs.model.exp import BaseModelWithRawArray
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
