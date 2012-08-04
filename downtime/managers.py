from django.db.models import Manager
from django.db.models.query import QuerySet
from datetime import datetime

class PeriodQuerySet(QuerySet):

    def active(self):
        return self.filter(enabled=True)

    def is_down(self):
        return self.filter(start_time__lte=datetime.now(), end_time__gte=datetime.now())

class PeriodManager(Manager):
    def get_query_set(self):
        return PeriodQuerySet(self.model, using=self._db)

    def active(self):
        return self.get_query_set().active()

    def is_down(self):
        return self.get_query_set().active().is_down()
