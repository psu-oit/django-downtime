from django.db import models
from django.utils.encoding import python_2_unicode_compatible


from downtime.managers import PeriodManager


@python_2_unicode_compatible
class Period(models.Model):
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    enabled = models.BooleanField(default=False)

    objects = PeriodManager()

    def __str__(self):
        return "Scheduled Downtime: %s to %s" % (self.start_time, self.end_time)
