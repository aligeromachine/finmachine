from money.models import Products, Catalog, Profit, Source, Buy, Shop

def update_products() -> None:
    data: dict = {str(it.state_id): it.pk for it in Catalog.objects.all()}
    for it in Products.objects.all():

        id = data[str(it.catalog_id)]
        Products.objects.filter(pk=it.pk).update(catalog_id=id)

def update_profit() -> None:
    data: dict = {str(it.state_id): it.pk for it in Source.objects.all()}
    for it in Profit.objects.all():
        id = data[str(it.source_id)]
        Profit.objects.filter(pk=it.pk).update(source_id=id)

def update_buy() -> None:
    data_shop: dict = {str(it.state_id): it.pk for it in Shop.objects.all()}
    data_prod: dict = {str(it.state_id): it.pk for it in Products.objects.all()}
    for it in Buy.objects.all():

        pk_shop = data_shop[str(it.shop_id)]
        pk_prod = data_prod[str(it.products_id)]

        Buy.objects.filter(pk=it.pk).update(shop_id=pk_shop, products_id=pk_prod)
