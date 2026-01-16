from django.contrib.auth.models import User
from django.db.models import Model

def RULES_ROUTE(user: str) -> list:
    for it in User.objects.filter(username=user):
        return str(it.last_name).split(',')
    return []

def is_super_user(user: str) -> bool:
    for it in User.objects.filter(username=user):
        return bool(it.is_superuser)
    return False

def UpdateSQl(query: str, values: list) -> None:
    from django.db import connection
    with connection.cursor() as cursor:
        cursor.execute(query, values)

def count_raw_sql(model: Model, sql: str, params: list) -> int:
    count: int = 0
    for it in model.objects.raw(raw_query=sql, params=params):
        count = it.c
    return count