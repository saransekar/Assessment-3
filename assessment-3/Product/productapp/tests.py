from django.test import TestCase
from .models import Client,ProductImplementation
# Create your tests here.
class ClientTestCase(TestCase):
	def setUp(self):
		client = Client.objects.create(client_name='Test',contact_name='Test',client_code='Test123',
		mobile_number='1234567890'
		)

		client.save()

	def test_get_client_details(self):
		client = Client.objects.get(id=39)
		expected_object_name = 'LIFTWELL EQUIPMENTS'
		self.assertEquals(client.client_name, expected_object_name) 	

	def test_get_product_details(self):
		client = Client.objects.get(id=39)
		product = ProductImplementation.objects.create(client_id=client,installation_date = 2011-11-11)
