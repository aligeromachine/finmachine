from django.urls import include, path

# flake8: noqa: E241
urlpatterns = [
    path(route='func/',     view=include('api.view.func.urls')),
    path(route='dash/',     view=include('api.view.dash.urls')),
    path(route='buy/',      view=include('api.view.buy.urls')),
    path(route='cards/',    view=include('api.view.cards.urls')),
    path(route='shop/',     view=include('api.view.shop.urls')),
    path(route='catalog/',  view=include('api.view.catalog.urls')),
    path(route='products/', view=include('api.view.products.urls')),
    path(route='source/',   view=include('api.view.source.urls')),
    path(route='profit/',   view=include('api.view.profit.urls')),
    path(route='logger/',   view=include('api.view.logger.urls')),
    path(route='etl/',      view=include('api.view.etl.urls')),
]
