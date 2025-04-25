from django.http import HttpRequest, JsonResponse
from money.libs.ext_c import (
    CONST,
    RequestEx)
from money.libs.ext_utils import DeltaDateTime
from api.back.func.main import (
    context_range_week,
    context_range_month,
    context_range_day)

def current_time(request: HttpRequest, *args, **kwargs):
    context = {RequestEx.data: DeltaDateTime(h=0).strftime(CONST.FTime)}
    return JsonResponse(context)

def current_date(request: HttpRequest, *args, **kwargs):
    context = {RequestEx.data: DeltaDateTime(h=0).strftime(CONST.FDate)}
    return JsonResponse(context)

def week_range(request: HttpRequest, *args, **kwargs):
    return JsonResponse(context_range_week())

def month_range(request: HttpRequest, *args, **kwargs):    
    return JsonResponse(context_range_month())

def day_range(request: HttpRequest, *args, **kwargs):
    return JsonResponse(context_range_day())
