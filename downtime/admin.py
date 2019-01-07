from django.conf import settings

# use admin only if not use DOWNTIME_NODATABASE_MODE
downtime_nodatbase_mode = getattr(settings, 'DOWNTIME_NODATABASE_MODE', False)
if not downtime_nodatbase_mode:
    from django.contrib import admin
    from downtime.models import Period

    admin.site.register(Period)
