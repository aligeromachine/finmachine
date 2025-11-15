import logging
from api.back.dash.model import DashboardMessage, DashSignal
from machine.func.model.calc import ReduceInfo

logger = logging.getLogger(__name__)

def base_info(item: DashboardMessage) -> dict:
    info: ReduceInfo = ReduceInfo.load_from_db(user_id=item.user_id)
    data: dict = DashSignal(**info.model_dump(exclude={'calcWgRange', 'calcWgYears', 'totalSumCards'})).to_dash()
    return data
