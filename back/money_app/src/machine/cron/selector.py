from machine.cron.query import GROUP_USER_YEAR_BUY_PROFIT
from money.models import Buy
from machine.cron.model import BuyGroup

def get_buy_group_by_year_user() -> list[BuyGroup]:
    ls: list = [BuyGroup.from_raw_query(raw_item=it) for it in Buy.objects.raw(raw_query=GROUP_USER_YEAR_BUY_PROFIT)]
    return ls
