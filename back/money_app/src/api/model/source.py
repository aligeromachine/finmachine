from api.model.main import MainModel

class SourceMessage(MainModel):
    offset: int
    limit: int
