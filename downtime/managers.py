import datetime

from django.db.models import Manager
from django.db.models.query import QuerySet
from django.conf import settings
from django.utils import timezone


class PeriodQuerySet(QuerySet):

    def active(self):
        return self.filter(enabled=True)

    def is_deployment(self):
        return self.filter(start_time__lte=timezone.now(), end_time=None)

    def is_down(self):
        return self.filter(start_time__lte=timezone.now(),
                           end_time__gte=timezone.now())


class PeriodManager(Manager):
    def get_queryset(self):
        return PeriodQuerySet(self.model, using=self._db)

    def active(self):
        return self.get_queryset().active()
    
    def is_deployment(self):
        return self.get_queryset().active().is_deployment()
        
    def is_down(self):
        return self.get_queryset().active().is_down() or self.get_queryset().active().is_deployment()
