from django.shortcuts import render, redirect
from django.conf import settings

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object


class DowntimeMiddleware(MiddlewareMixin):
    def process_request(self, request):
        downtime_mixin = getattr(settings, 'DOWNTIME_MIXIN', None)

        if downtime_mixin:
            import importlib
            for mixin in downtime_mixin:
                mod_name, func_name = mixin.rsplit('.', 1)
                mod = importlib.import_module(mod_name)
                func = getattr(mod, func_name)
                result = func(self, request)
                if not result:
                    return None

        exempt_exact_urls = getattr(settings, 'DOWNTIME_EXEMPT_EXACT_URLS', None)
        if exempt_exact_urls:
            for url in exempt_exact_urls:
                if request.path == url:
                    return None

        exempt_paths = getattr(settings, 'DOWNTIME_EXEMPT_PATHS', ('/admin',))
        for path in exempt_paths:
            if request.path.startswith(path):
                return None

        downtime_nodatbase_mode = getattr(settings, 'DOWNTIME_NODATABASE_MODE', False)
        if not downtime_nodatbase_mode:
            from downtime.models import Period
            objects = Period.objects.is_down()

        if downtime_nodatbase_mode or objects.count():
            # we are down.
            url_redirect = getattr(settings, 'DOWNTIME_URL_REDIRECT', None)
            if url_redirect:
                return redirect(url_redirect)
            else:
                return render(request, "downtime/downtime.html", status=503)
