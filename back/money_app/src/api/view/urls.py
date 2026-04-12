from django.urls import path
from api.view.respo import buy_respo, dash_respo, logger_respo, version_respo, source_respo, shop_respo, profit_respo, \
    catalog_respo, cards_respo, products_respo, etl_respo

# flake8: noqa: E241
urlpatterns = [
    path(route='version/', view=version_respo),
    path(route='dash/', view=dash_respo),
    path(route='buy/', view=buy_respo), 
    path(route='cards/', view=cards_respo),
    path(route='shop/', view=shop_respo),
    path(route='catalog/', view=catalog_respo),
    path(route='products/', view=products_respo),
    path(route='source/', view=source_respo),
    path(route='profit/', view=profit_respo),
    path(route='logger/', view=logger_respo),
    path(route='etl/<str:name>', view=etl_respo),
]
