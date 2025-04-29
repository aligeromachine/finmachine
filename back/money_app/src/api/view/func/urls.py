from django.urls import path
from api.view.func.views import (
    current_time,
    current_date,
    week_range,
    month_range,
    day_range)


urlpatterns = [
    path('current_time', current_time, name='current_time'),
    path('current_date', current_date, name='current_date'),
    path('week_range', week_range, name='week_range'),
    path('month_range', month_range, name='month_range'),
    path('day_range', day_range, name='day_range'),
]
