from datetime import datetime
from api.back.model import BaseMessage, BaseSelector
from libs.model.exp import BaseModelWithRawArray

class CatalogMessage(BaseMessage):
    pass

class CatSignal(BaseModelWithRawArray):
    title: str
    created: datetime

class CatSignalKV(BaseModelWithRawArray):
    id: int
    title: str

class CatSelector(BaseSelector):
    pass
