import datetime


from django.test import TransactionTestCase

from downtime.tests.factories import PeriodFactory
from downtime.models import Period


class DowntimeModelTest(TransactionTestCase):

    def setUp(self):
        self.period = PeriodFactory.create()

    def test_active(self):
        self.assertTrue(Period.objects.active().count())

    def test_inactive(self):
        self.period.enabled = False
        self.period.save()

        self.assertFalse(Period.objects.active().count())

    def test_is_down(self):
        self.assertTrue(Period.objects.is_down().count())

    def test_is_not_down(self):
        self.period.start_time = datetime.datetime.now() - datetime.timedelta(days=4)
        self.period.end_time = datetime.datetime.now() - datetime.timedelta(days=1)
        self.period.save()

        self.assertFalse(Period.objects.is_down().count())



