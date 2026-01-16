from datetime import datetime
from api.back.decore import BaseMessage, BaseSelector
from libs.model.exp import BaseModelWithRawArray

class SourceMessage(BaseMessage):
    pass

class SourceSignal(BaseModelWithRawArray):
    title: str
    created: datetime

class SourceSignalKV(BaseModelWithRawArray):
    id: int
    title: str

class SourceSelector(BaseSelector):
    pass
