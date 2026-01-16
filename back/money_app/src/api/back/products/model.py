from datetime import datetime
from pydantic import Field
from api.back.decore import BaseMessage, BaseSelector
from libs.model.exp import BaseModelWithRawArray

class ProductsMessage(BaseMessage):
    catalog: int = 0

class ProdSignal(BaseModelWithRawArray):
    title: str
    catalog: int = Field(..., alias="catalog_id")
    created: datetime

class ProdSignalKV(BaseModelWithRawArray):
    id: int
    title: str

class ProdSelector(BaseSelector):
    catalog: str
