import logging
from machine.cron.selector import get_buy_group_by_year_user
from machine.cron.model import BuyGroup

logger = logging.getLogger(__name__)

def machine_aggregation() -> None:

    ls: list[BuyGroup] = get_buy_group_by_year_user()
    for item in ls:

        pass
