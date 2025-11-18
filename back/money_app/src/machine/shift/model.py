from datetime import datetime
from decimal import Decimal
import functools
from typing import Callable
from pydantic import BaseModel
from api.back.buy.model import BuyMessage
from back.money_app.src.machine.shift.writer import rewrite_payload
from back.money_app.src.machine.tools.model import WidgetRange
from back.money_app.src.machine.tools.selector import get_user_date_range
from money.libs.cache.redis import RedisClient
from money.libs.types.exp import F_Return, F_Spec

class BaseSignal(BaseModel):
    amount: Decimal
    created: datetime

class MacShift:
    KEY_BUY: str = 'row_buy_user_id'

    @staticmethod
    def row_save_redis(func: Callable[..., F_Return]) -> Callable[..., F_Return]:
        @functools.wraps(func)
        def wrapper(*args: F_Spec.args, **kwargs: F_Spec.kwargs) -> F_Return:

            model: BuyMessage = kwargs['item']
            result = func(*args, **kwargs)
            signal: BaseSignal = BaseSignal(**result)

            if model.command == 'get_buy_row':
                raw: str = f'{MacShift.KEY_BUY}_{model.user_id}'
                with RedisClient() as red:

                    if red.exists_key(key=raw):
                        red.delete_key(key=raw)

                    red.set_key_json(key=raw, value=signal.model_dump())
            return result
        return wrapper

    @staticmethod
    def raw_add_buy_data(func: Callable[..., F_Return]) -> Callable[..., F_Return]:
        @functools.wraps(func)
        def wrapper(*args: F_Spec.args, **kwargs: F_Spec.kwargs) -> F_Return:

            model: BuyMessage = kwargs['item']
            result = func(*args, **kwargs)

            rng: list[WidgetRange] = get_user_date_range(user_id=model.user_id)
            for it in rng:
                if it.dt == model.created.year:
                    it.buy += model.amount

            rewrite_payload(user_id=model.user_id, rng=rng)

            return result
        return wrapper
