from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Client(models.Model):
	client_name = models.CharField(max_length=20)
	contact_name = models.CharField(max_length=20)
	client_code = models.CharField(max_length=15,unique=True)
	mobile_number = models.CharField(max_length=10)

	def __str__(self):
		return str(self.client_name)

	class Meta:
		db_table = "client"


class ProductImplementation(models.Model):
	client = models.ForeignKey(Client, on_delete=models.CASCADE,null=True)
	installation_date = models.DateField()

	def __str__(self):
		return str(self.installation_date)

	class Meta:
		db_table = "product_implementation"			 


class Router(models.Model):
	client = models.ForeignKey(Client, on_delete=models.CASCADE,null=True)
	wireless_router_ip = models.CharField(max_length=30)

	def __str__(self):
		return str(self.wireless_router_ip)

	class Meta:
		db_table = "router"

		
class Hub(models.Model):
	client = models.ForeignKey(Client, on_delete=models.CASCADE,null=True)
	hub_ip = models.CharField(max_length=30)

	def __str__(self):
		return str(self.hub_ip)

	class Meta:
		db_table = "hub"