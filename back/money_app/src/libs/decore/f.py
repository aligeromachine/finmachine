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
