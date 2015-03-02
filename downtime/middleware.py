from django.shortcuts import render, redirect
from django.conf import settings

from downtime.models import Period


class DowntimeMiddleware(object):
    def process_request(self, request):
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

