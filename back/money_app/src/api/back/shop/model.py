from datetime import datetime
import logging
from api.back.model import BaseMessage, BaseSelector
from libs.model.exp import BaseModelWithRawArray

logger = logging.getLogger(__name__)

class ShopMessage(BaseMessage):
    address: str = ''

class ShopSignal(BaseModelWithRawArray):
    title: str
    address: str
    created: datetime

class ShopSignalKV(BaseModelWithRawArray):
    id: int
    title: str

class ShopSelector(BaseSelector):
    address: str
