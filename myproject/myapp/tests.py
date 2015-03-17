from django.test import TestCase
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
import json
# Create your tests here.
class firstPageTestCase(TestCase):
    def test_index(self):
        resp = self.client.get('/import/')
	self.assertEqual(resp.status_code, 200)


class getcontacsTestCase(TestCase):
    def test_index(self):
        resp = self.client.get('/gmailContacts/')
	self.assertEqual(resp.status_code, 200)

class postContacts(TestCase):
  def test_your_test(self):
        python_dict = {
            "user": "shrikant", "contacts":"shrikant" 
        }
        resp = self.client.post('/gmailContacts/',
                                    json.dumps(python_dict),
                                    content_type="application/json")
	self.assertEqual(resp.status_code, 201)
