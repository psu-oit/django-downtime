from django.test import TestCase

from downtime.models import Period
from downtime.tests.factories import PeriodFactory

from django.core.management import call_command

class DowntimeCommandsTest(TestCase):

    def setUp(self):
        self.period = PeriodFactory.create()

    def test_inital_active(self):
        self.assertTrue(Period.objects.is_down(), \
            'Period should deployed initially.')

    def test_downtime_end(self):
        call_command('downtime_end')
        deployed_periods = Period.objects.is_deployment()
        self.assertFalse(deployed_periods, \
            'After running downtime_end, the period should not be deployed.\n \
            Returned: %s ' % deployed_periods)

    def test_downtime_start(self):
        call_command('downtime_start')
        deployed_periods = Period.objects.is_deployment()
        self.assertTrue(deployed_periods,\
            'After running downtime_start, the period should be deployed.\n \
            Returned: %s ' % deployed_periods)
