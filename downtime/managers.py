import datetime

from django.db.models import Manager
from django.db.models.query import QuerySet
from django.conf import settings
from django.utils.timezone import utc


class PeriodQuerySet(QuerySet):

    def active(self):
        return self.filter(enabled=True)
    
    def is_deployment(self):
        if getattr(settings, 'USE_TZ', False):
            return self.filter(start_time__lte=datetime.datetime.utcnow().replace(tzinfo=utc), 
                               end_time=None)
        else:
            return self.filter(start_time__lte=datetime.datetime.now(), 
                               end_time=None)
        
    def is_down(self):
        if getattr(settings, 'USE_TZ', False):
            return self.filter(start_time__lte=datetime.datetime.utcnow().replace(tzinfo=utc), 
                               end_time__gte=datetime.datetime.utcnow().replace(tzinfo=utc))
        else:
            return self.filter(start_time__lte=datetime.datetime.now(), 
                               end_time__gte=datetime.datetime.now())


class PeriodManager(Manager):
    def get_queryset(self):
        return PeriodQuerySet(self.model, using=self._db)

    def active(self):
        return self.get_queryset().active()
    
    def is_deployment(self):
        return self.get_queryset().active().is_deployment()
        
    def is_down(self):
        return self.get_queryset().active().is_down() or self.get_queryset().active().is_deployment()
