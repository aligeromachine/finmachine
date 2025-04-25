from django.http import HttpRequest, HttpResponse
from django.template import loader

def main_template(request: HttpRequest, *args, **kwargs):

    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render({}, request))
