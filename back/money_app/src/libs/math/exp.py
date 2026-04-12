from decimal import Decimal
# from pydantic import BaseModel
from libs.types.exp import TBaseModel
from collections import defaultdict
from typing import Callable

def trim_decimal(value: Decimal) -> Decimal:
    """Using Decimal for precise decimal arithmetic"""
    return value.quantize(Decimal(1)) if value == value.to_integral() else value.normalize()

def group_by(
        objects: list[TBaseModel], 
        group_by_field: str | Callable, 
        agg_fields: dict[str, list[Callable]], 
        ignore_zero: bool = True) -> list:

    if isinstance(group_by_field, str):
        key_func = lambda obj: getattr(obj, group_by_field)
    else:
        key_func = group_by_field

    groups = defaultdict(list)
    for obj in objects:
        key = key_func(obj)
        groups[key].append(obj)

    # Агрегация
    result = []
    for key, group in groups.items():
        row = {'group_key': key}

        for field, agg_funcs in agg_fields.items():
            values = [getattr(obj, field) for obj in group if getattr(obj, field) != 0] if ignore_zero else [getattr(obj, field) for obj in group]
            for agg_func in agg_funcs:
                func_name = agg_func.__name__
                col_name = f"{field}_{func_name}"
                row[col_name] = agg_func(values)

        result.append(row)

    return result

def total_summary(objects: list[TBaseModel], agg_fields: dict[str, list[Callable]], ignore_zero: bool = True) -> dict:
    if agg_fields is None:
        agg_fields = {}

    result = {}

    for field, agg_funcs in agg_fields.items():

        values = []
        for obj in objects:

            if ignore_zero:
                if getattr(obj, field) == 0:
                    continue

            if hasattr(obj, field):
                values.append(getattr(obj, field))

        for agg_func in agg_funcs:

            func_name = agg_func.__name__
            col_name = f"{field}_{func_name}"

            if not values:
                result[col_name] = 0
            else:
                result[col_name] = agg_func(values)

    return result

# if __name__ == '__main__':

#     class Product(BaseModel):
#         category: str
#         price: int
#         quantity: int

#     # Данные
#     products = [
#         Product(category="Electronics", price=1000, quantity=5),
#         Product(category="Clothing", price=30, quantity=20),
#         Product(category="Electronics", price=500, quantity=10),
#         Product(category="Electronics", price=250, quantity=24),
#         Product(category="Books", price=50, quantity=15),
#         Product(category="Books", price=254, quantity=15),
#         Product(category="Books", price=50, quantity=15),
#         Product(category="Clothing", price=75, quantity=0),
#     ]

#     # Группировка по category
#     result = group_by(
#         products,
#         group_by_field="category",
#         agg_fields={
#             'price': [sum, len],
#             'quantity': [sum, len],
#         }
#     )

#     for r in result:
#         print(f"Category: {r['group_key']}")
#         print(f"  Sum price: {r['price_sum']}")
#         print(f"  Len price: {r['price_len']}")
#         print("***")
#         print(f"  Sum quantity: {r['quantity_sum']}")
#         print(f"  Len quantity: {r['quantity_len']}")
#         print("=========")
#         print(r)

#     # Подсчет сумм по всей таблице
#     total = total_summary(
#         products,
#         agg_fields={
#             'price': [sum, len],
#             'quantity': [sum, len]
#         }
#     )

#     print("Total summary:")
#     print(f"  Total price (sum): ${total['price_sum']}")
#     print(f"  Len price: ${total['price_len']}")
#     print(f"  Total quantity: {total['quantity_sum']}")
#     print(f"  Len quantity: {total['quantity_len']}")
