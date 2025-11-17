from decimal import Decimal
from money.libs.model.exp import BaseModelWithRawArray

class WidgetRange(BaseModelWithRawArray):
    dt: int
    buy: Decimal
    profit: Decimal
