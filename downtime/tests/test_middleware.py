from mock import Mock

from django.test import TestCase


from downtime.middleware import DowntimeMiddleware
from downtime.tests.factories import PeriodFactory


class DowntimeMiddlewareTest(TestCase):

    def setUp(self):
        self.dm = DowntimeMiddleware()
        self.request = Mock()
        self.request.session = {}
        self.period = PeriodFactory.create()

    def test_exempt_exact_urls(self):
        self.request.path = '/test/page/id'
        self.assertTrue(self.dm.process_request(self.request))

        with self.settings(DOWNTIME_EXEMPT_EXACT_URLS=('/test/page/id', )):
            self.assertIsNone(self.dm.process_request(self.request))

            self.request.path = '/test/page/id/child'
            self.assertTrue(self.dm.process_request(self.request),
                            'Children pages are not exempted to exact urls')

    def test_exempt_paths(self):
        self.request.path = '/admin'
        self.assertIsNone(self.dm.process_request(self.request))

    def test_render(self):
        self.request.path = '/'
        response = self.dm.process_request(self.request)
        self.assertEqual(response.status_code, 503)
