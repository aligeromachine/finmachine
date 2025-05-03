from api.model.main import MainModel

class ShopMessage(MainModel):
    pk: int = 0
    offset: int = 0
    limit: int = 0
    title: str = ''
    address: str = ''
