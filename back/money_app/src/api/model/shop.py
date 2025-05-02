from api.model.main import MainModel

class ShopMessage(MainModel):
    offset: int = 0
    limit: int = 0
    title: str = ''
    address: str = ''
