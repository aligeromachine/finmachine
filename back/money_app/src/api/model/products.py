from api.model.main import MainModel

class ProductsMessage(MainModel):
    pk: int = 0
    offset: int = 0
    limit: int = 0
    title: str = ''
    catalog: int = 0
