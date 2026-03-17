from django.http import HttpResponseForbidden, HttpResponsePermanentRedirect
from django.utils import translation
from django.shortcuts import redirect
from django.urls import reverse
import datetime
import re

class RequestLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(f"[{datetime.datetime.now()}] {request.method} {request.path}")
        response = self.get_response(request)
        return response
    
class SecurityHeadersMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['X-Frame-Options'] = 'DENY'
        response['X-Content-Type-Options'] = 'nosniff'
        response['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
        return response
    

class IPBlockMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    
    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        if ip in self.BLOCKED_IPS:
            return HttpResponseForbidden('Доступ запрещен')
        return self.get_response(request)
    

class MinifyHTMLMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if "text/html" in response ["Content-Type"]:
            response.content = re.sub(r"\s+", " ", response.content.decode("utf-8")).encode("utf-8")
        return response
    

class ForceHTTPSMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.is_secure():
            return HttpResponsePermanentRedirect(f"https://{request.get_host()}{request.get_full_path()}")
        return self.get_response(request)
    

class LocalMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        language = request.META.get("HTTP_ACCEPT_LANGUAGE", "en").split(",")[0]
        translation.activate(language)
        request.LANGUAGE_CODE = language
        response = self.get_response(request)
        translation.deactivate()
        return response
    

class LoginRequiredMiddleware:
    EXCLUDED_PATHS = ["/login/", "/register/"]

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and request.path not in self.EXCLUDED_PATHS:
            return redirect(reverse("login"))
        return self.get_response(request)