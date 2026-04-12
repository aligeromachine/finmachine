from typing import Any
from django.http import HttpRequest, HttpResponse
from django.template import loader

def main_template(request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render({}, request))
