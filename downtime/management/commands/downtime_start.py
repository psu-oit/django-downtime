from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.utils.timezone import utc

import datetime

from downtime.models import Period

class Command(BaseCommand):
    help = 'Start downtime due to maintenance/deployment/whatever.'

    def handle(self, *args, **options):
        if getattr(settings, 'USE_TZ', False):
            p = Period(enabled=True, start_time=datetime.datetime.utcnow().replace(tzinfo=utc))
        else:
            p = Period(enabled=True, start_time=datetime.datetime.now())
        p.save()
        self.stdout.write('Successfully started downtime')
