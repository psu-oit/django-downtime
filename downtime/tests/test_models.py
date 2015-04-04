from django.test import TestCase

from downtime.tests.factories import PeriodFactory
from downtime.models import Period


class DowntimeModelTest(TestCase):

    def setUp(self):
        self.period = PeriodFactory.create()

    def test_unicode(self):
        self.assertEqual(self.period.__unicode__(), 'Scheduled downtime')

    def test_active(self):
        self.assertTrue(Period.objects.active().count())

    def test_inactive(self):
        self.period.enabled = False
        self.period.save()

        self.assertFalse(Period.objects.active().count())


