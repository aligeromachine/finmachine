from decimal import Decimal

from pydantic import Field
from money.libs.model.exp import BaseModelWithRawArray

class WidgetRange(BaseModelWithRawArray):
    dt: int
    buy: Decimal
    profit: Decimal

class WidgetYear(WidgetRange):
    dt: int = Field(..., alias="year") 
