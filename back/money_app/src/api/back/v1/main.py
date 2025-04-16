from django.http import HttpRequest
from api.back.model import parse_model, MetaComment


def task_status(item: MetaComment):
    respo = {'data': 'err', 'message': f'task: {item.payload} not'}

    return respo


def task_resolve(item: MetaComment):
    respo = {'data': 'err', 'message': f'task: {item.payload} not'}

    return respo


@parse_model(MetaComment)
def task_response(request: HttpRequest, item: MetaComment):
    respo = {'data': 'err', 'message': 'undefinded'}

    if item.command == "status":
        respo = task_status(item=item)

    if item.command == "resolve":
        respo = task_resolve(item=item)

    ls = []
    ls.append({
        "name": "Joe Silver",
        "email": "joe@email.com",
        "document": "22342342",
        "phone": "00000000"

    })

    return ls
