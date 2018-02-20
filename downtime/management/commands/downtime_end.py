from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.utils import timezone

import datetime

from downtime.models import Period

class Command(BaseCommand):
    help = 'End downtime after finished maintenance/deployment/whatever.'

    def handle(self, *args, **options):
        objects = Period.objects.is_deployment()
        _now = timezone.now()
        for obj in objects:
            obj.end_time = _now
            obj.save()

        self.stdout.write('Successfully ended downtime')
