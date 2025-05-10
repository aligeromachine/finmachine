from api.model.main import MainModel

class ProfitMessage(MainModel):
    pk: int = 0
    offset: int = 0
    limit: int = 0
    title: str = ''
    sources: int = 0
