from api.model.main import MainModel

class CatalogMessage(MainModel):
    pk: int = 0
    offset: int = 0
    limit: int = 0
    title: str = ''
