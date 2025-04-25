from api.model.main import MainModel

class CatalogMessage(MainModel):
    offset: int
    limit: int
