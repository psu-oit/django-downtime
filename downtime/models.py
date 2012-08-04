from django.db import models

class Period(models.Model):
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    url_redirect = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return "Scheduled downtime"