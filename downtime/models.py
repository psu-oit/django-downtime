from django.db import models
from downtime.managers import PeriodManager

class Period(models.Model):
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    enabled = models.BooleanField()

    objects = PeriodManager()

    def __unicode__(self):
        return "Scheduled downtime"