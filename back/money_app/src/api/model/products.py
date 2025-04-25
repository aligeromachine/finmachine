from api.model.main import MainModel

class ProductsMessage(MainModel):
    offset: int
    limit: int
