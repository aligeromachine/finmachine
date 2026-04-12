from api.back.model import MainModel
from machine.dash.model import Capital, CardsAgg, DateRng, TopTitle
from libs.model.exp import BaseModelWithRawArray
import logging
from pydantic import Field

logger = logging.getLogger(__name__)

class DashboardMessage(MainModel):
    pass

class DashSignal(BaseModelWithRawArray):
    capital: Capital = Capital()
    cards: CardsAgg = CardsAgg()
    profit: DateRng = DateRng()
    buy: DateRng = DateRng()

    daily: list[TopTitle] = Field(..., alias='topDaily')
    shop: list[TopTitle] = Field(..., alias='topShop')

    def to_dash(self) -> dict:
        data: dict = dict(
            capital=self.capital.model_dump(),
            cards=self.cards.model_dump(),
            profit=self.profit.model_dump(),
            buy=self.buy.model_dump(),
            daily=[it.model_dump() for it in self.daily],
            shop=[it.model_dump() for it in self.shop],
        )
        return data
