from django.test import TestCase

# Create your tests here.
class firstPageTestCase(TestCase):
    def test_index(self):
        resp = self.client.get('/import/')
	self.assertEqual(resp.status_code, 200)


class getcontacsTestCase(TestCase):
    def test_index(self):
        resp = self.client.get('/gmailContacts/')
	self.assertEqual(resp.status_code, 200)
