from django import forms  
from productapp.models import Client  
from productapp.models import ProductImplementation
from productapp.models import Router
from productapp.models import Hub
from django.core.exceptions import ValidationError

class ClientForm(forms.ModelForm):
	class Meta:
		model = Client
		fields = ['client_name', 'contact_name', 'client_code', 'mobile_number']

	def clean_client_code(self):
		
		client_code = self.cleaned_data['client_code']
		client = Client.objects.filter(client_code=client_code)
		if client.count():
			raise ValidationError("client code already exists")
		return client_code
	
class ProductForm(forms.ModelForm):
	class Meta:
		model = ProductImplementation
		fields = ['installation_date']

class RouterForm(forms.ModelForm):
	class Meta:
		model = Router
		fields = ['wireless_router_ip']


class HubForm(forms.ModelForm):
	class Meta:
		model = Hub
		fields = ['hub_ip']