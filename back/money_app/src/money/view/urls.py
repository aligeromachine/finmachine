from django.urls import path
from money.view.view import (
    main_template)

urlpatterns = [
    path('', main_template, name='dashboard'),
]
