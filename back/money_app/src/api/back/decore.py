from functools import wraps

def draw_response(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        ls, count, offset, limit = func(*args, **kwargs)
        result: dict = {
            'recordsTotal': count,
            'offset': offset,
            'recordsDisplay': limit,
            'draw': ls
        }
        return result
    return wrapper
