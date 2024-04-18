from django.test import TestCase, SimpleTestCase

class SimpleTest(SimpleTestCase):
    def test_introduction(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

