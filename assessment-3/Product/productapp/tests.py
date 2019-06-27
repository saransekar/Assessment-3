
from django.test import TestCase
from productapp.models import Client,ProductImplementation

# Create your tests here.
class ClientTestCase(TestCase):
	def setUp(self):
		client = Client.objects.create(client_name="Test",contact_name="Test",client_code="Test123",
		mobile_number="1234567890")
		product = ProductImplementation.objects.create()

	def test_get_client_details(self):
		client = Client.objects.get(client_name="Test")
		expected_object_name = 'Test'
		self.assertEquals(client.client_name, expected_object_name) 	

	def test_get_product_details(self):
		client = Client.objects.get(client_code="Test123")
		client_id = client_id.id
		product = ProductImplementation.objects.create(client_id=client_id,installation_date = 2011-11-11)
		self.assertEquals(product.installation_date,  '2011-11-11')

	def test_get_router_details(self):
		client = Client.objects.get(client_code="Test123")
		client_id = client_id.id
		router = router.objects.create(client_id=client_id,wireless_router_ip = '192.00.1200')
		self.assertEquals(router.wireless_router_ip,  '192.00.1200')
	

	def test_get_hub_details(self):
		client = Client.objects.get(client_code="Test123")
		client_id = client_id.id
		hub = hub.objects.create(client_id=client_id,hub_ip = '192.00.1200')
		self.assertEquals(hub.hub_ip,  '192.00.1200')	
		 