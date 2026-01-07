from datetime import datetime
from decimal import Decimal
import functools
from typing import Callable
from pydantic import BaseModel
from api.back.buy.model import BuyMessage
from machine.shift.selector import get_buy_amount_by_id
from machine.shift.writer import rewrite_payload
from machine.tools.model import WidgetRange
from machine.tools.selector import get_list_user_finance
from money.libs.cache.redis import RedisClient
from money.libs.types.exp import F_Return, F_Spec

class BaseSignal(BaseModel):
    amount: float
    created: datetime

class MacBuyShift:
    key_redis: str = 'row_buy_id'
    cmd_add: str = 'add_buy_data'
    cmd_del: str = 'delete_buy_row'

    @staticmethod
    def row_save_redis(func: Callable[..., F_Return]) -> Callable[..., F_Return]:
        @functools.wraps(func)
        def wrapper(*args: F_Spec.args, **kwargs: F_Spec.kwargs) -> F_Return:

            model: BuyMessage = kwargs['item']
            result = func(*args, **kwargs)
            signal: BaseSignal = BaseSignal(**result)

            raw: str = f'{MacBuyShift.key_redis}_{model.pk}'
            with RedisClient() as red:
                red.set_key_json(key=raw, value=signal.model_dump())
            return result
        return wrapper

    @staticmethod
    def row_change(func: Callable[..., F_Return]) -> Callable[..., F_Return]:
        @functools.wraps(func)
        def wrapper(*args: F_Spec.args, **kwargs: F_Spec.kwargs) -> F_Return:

            model: BuyMessage = kwargs['item']
            rng: list[WidgetRange] = get_list_user_finance(user_id=model.user_id)
            if model.created.year in [kt.dt for kt in rng]:
                for it in rng:
                    if it.dt == model.created.year:
                        if model.command == MacBuyShift.cmd_add:
                            it.buy += model.amount
                        if model.command == MacBuyShift.cmd_del:
                            it.buy -= get_buy_amount_by_id(pk=model.pk)
            else:
                buy: Decimal = Decimal(0)
                if model.command == MacBuyShift.cmd_add:
                    buy += model.amount
                if model.command == MacBuyShift.cmd_del:
                    buy -= get_buy_amount_by_id(pk=model.pk)
                draw = WidgetRange(dt=model.created.year, buy=buy)
                rng.append(draw)

            rewrite_payload(user_id=model.user_id, rng=rng)

            return func(*args, **kwargs)
        return wrapper

    @staticmethod
    def row_edit(func: Callable[..., F_Return]) -> Callable[..., F_Return]:
        @functools.wraps(func)
        def wrapper(*args: F_Spec.args, **kwargs: F_Spec.kwargs) -> F_Return:

            model: BuyMessage = kwargs['item']
            rng: list[WidgetRange] = get_list_user_finance(user_id=model.user_id)

            raw: str = f'{MacBuyShift.key_redis}_{model.pk}'
            with RedisClient() as red:

                signal: BaseSignal = BaseSignal(**red.get_key_json(key=raw))
                red.delete_key(key=raw)

                for it in rng:
                    if it.dt == model.created.year:
                        it.buy += model.amount
                    if it.dt == signal.created.year:
                        it.buy -= Decimal(signal.amount)

                rewrite_payload(user_id=model.user_id, rng=rng)

            return func(*args, **kwargs)
        return wrapper
