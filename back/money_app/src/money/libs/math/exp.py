from decimal import Decimal

def trim_decimal(value: Decimal) -> Decimal:
    """Using Decimal for precise decimal arithmetic"""
    return value.quantize(Decimal(1)) if value == value.to_integral() else value.normalize()
