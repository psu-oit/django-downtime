import datetime

from django.utils import timezone
import factory

from downtime.models import Period


class PeriodFactory(factory.DjangoModelFactory):
    start_time = timezone.now()
    end_time = timezone.now() + datetime.timedelta(days=2)
    enabled = True

    class Meta:
        model = Period
