import factory
import datetime

from downtime.models import Period


class PeriodFactory(factory.DjangoModelFactory):
    start_time = datetime.datetime.now()
    end_time = datetime.datetime.now() + datetime.timedelta(days=2)
    enabled = True

    class Meta:
        model = Period
