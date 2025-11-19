from datetime import datetime
from decimal import Decimal
import functools
from typing import Callable
from pydantic import BaseModel
from api.back.buy.model import BuyMessage
from machine.shift.writer import rewrite_payload
from machine.tools.model import WidgetRange
from machine.tools.selector import get_list_user_finance
from money.libs.cache.redis import RedisClient
from money.libs.types.exp import F_Return, F_Spec

class BaseSignal(BaseModel):
    amount: Decimal
    created: datetime

class MacShift:
    KEY_BUY: str = 'row_buy_user_id'
    cmd_add: str = 'add_buy_data'
    cmd_del: str = 'delete_buy_row'

    @staticmethod
    def row_save_redis(func: Callable[..., F_Return]) -> Callable[..., F_Return]:
        @functools.wraps(func)
        def wrapper(*args: F_Spec.args, **kwargs: F_Spec.kwargs) -> F_Return:

            model: BuyMessage = kwargs['item']
            result = func(*args, **kwargs)
            signal: BaseSignal = BaseSignal(**result)

            raw: str = f'{MacShift.KEY_BUY}_{model.user_id}'
            with RedisClient() as red:

                if red.exists_key(key=raw):
                    red.delete_key(key=raw)

                red.set_key_json(key=raw, value=signal.model_dump())
            return result
        return wrapper

    @staticmethod
    def row_change_buy_data(func: Callable[..., F_Return]) -> Callable[..., F_Return]:
        @functools.wraps(func)
        def wrapper(*args: F_Spec.args, **kwargs: F_Spec.kwargs) -> F_Return:

            model: BuyMessage = kwargs['item']
            rng: list[WidgetRange] = get_list_user_finance(user_id=model.user_id)
            for it in rng:
                if it.dt == model.created.year:
                    if model.command == MacShift.cmd_add:
                        it.buy += model.amount
                    if model.command == MacShift.cmd_del:
                        it.buy -= model.amount  # get in model amount
            rewrite_payload(user_id=model.user_id, rng=rng)

            return func(*args, **kwargs)
        return wrapper
