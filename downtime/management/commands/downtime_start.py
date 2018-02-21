from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.utils import timezone

import datetime

from downtime.models import Period

class Command(BaseCommand):
    help = 'Start downtime due to maintenance/deployment/whatever.'

    def handle(self, *args, **options):
        p = Period(enabled=True, start_time=timezone.now())
        p.save()
        self.stdout.write('Successfully started downtime')
