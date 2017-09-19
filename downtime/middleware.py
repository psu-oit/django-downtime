from django.shortcuts import render, redirect
from django.conf import settings

from downtime.models import Period

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object


class DowntimeMiddleware(MiddlewareMixin):
    def process_request(self, request):
        exempt_exact_urls = getattr(settings,
                                    'DOWNTIME_EXEMPT_EXACT_URLS', None)
        if exempt_exact_urls:
            for url in exempt_exact_urls:
                if request.path == url:
                    return None

        exempt_paths = getattr(settings, 'DOWNTIME_EXEMPT_PATHS', ('/admin',))
        for path in exempt_paths:
            if request.path.startswith(path):
                return None

        objects = Period.objects.is_down()

        if objects.count():
            # we are down.
            url_redirect = getattr(settings, 'DOWNTIME_URL_REDIRECT', None)
            if url_redirect:
                return redirect(url_redirect)
            else:
                return render(request, "downtime/downtime.html", status=503)
