# middleware.py
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse

class NoCacheMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        response: HttpResponse = self.get_response(request)
        
        if request.user.is_authenticated:
            # Add headers to prevent caching of authenticated pages
            response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
            response['Pragma'] = 'no-cache'
            response['Expires'] = '0'
        else:
            # Redirect to login if accessing protected page while logged out
            protected_paths = ['/dashboard/', '/account/']  # Add your protected paths
            if any(request.path.startswith(path) for path in protected_paths):
                return HttpResponseRedirect(f"{reverse('login')}?next={request.path}")
        
        return response
