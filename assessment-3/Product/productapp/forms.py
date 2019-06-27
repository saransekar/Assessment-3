from django import forms  
from productapp.models import Client, ProductImplementation, Router, Hub  
from django.core.exceptions import ValidationError

class DateInput(forms.DateInput):
	input_type = 'date'

class ClientForm(forms.ModelForm):
	client_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter client name'}), required=True)
	contact_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter contact name'}), required=True)
	client_code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter client code'}), required=True)		
	mobile_number = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter mobile number'}), required=True)
	class Meta:
		model = Client 
		fields = ('client_name', 'contact_name', 'client_code', 'mobile_number',)

            
class ProductForm(forms.ModelForm):
	
	installation_date = forms.DateField(widget=DateInput)
	class Meta:
		model = ProductImplementation
		fields = ('installation_date',)
		widgets = {
            'installation_date': forms.DateInput(attrs={'class': 'form-control'}),
        }		
		

class RouterForm(forms.ModelForm):
	class Meta:
		model = Router
		fields = ('wireless_router_ip',)

		widgets = {
            'wireless_router_ip': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter router name'}),
        }

class HubForm(forms.ModelForm):
	class Meta:
		model = Hub
		fields = ('hub_ip',)
		widgets = {
            'hub_ip': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter hub name'}),
        }





