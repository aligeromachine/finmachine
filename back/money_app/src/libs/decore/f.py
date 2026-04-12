def dropwhile(sorted_dict: dict, query: str) -> dict:
    if not query:
        return sorted_dict

    index = 0
    for i, (key, v) in enumerate(sorted_dict.items()):
        if key == query:
            index = i
            break

    if not index:
        return sorted_dict

    return {key: v for i, (key, v) in enumerate(sorted_dict.items()) if index <= i}


def check_range(value: int, range_limits: tuple[int, int], mode: str = 'inclusive') -> bool:
    """
    Проверяет вхождение числа в диапазон
    Args:
        value: проверяемое число
        range_limits: кортеж (min, max) или список [min, max]
        mode: 'strict' (исключая границы), 
              'inclusive' (включая), 
              'left' (левая включена), 
              'right' (правая включена)
    """
    min_val, max_val = sorted(range_limits)

    modes = {
        'strict': lambda v: min_val < v < max_val,
        'inclusive': lambda v: min_val <= v <= max_val,
        'left': lambda v: min_val <= v < max_val,
        'right': lambda v: min_val < v <= max_val
    }

    if mode not in modes:
        raise ValueError(f"Неверный режим. Доступны: {list(modes.keys())}")

    return bool(modes[mode](value))
