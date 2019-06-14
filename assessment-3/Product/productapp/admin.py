from django.contrib import admin
from .models import Client
from .models import ProductImplementation
from .models import Router
from .models import Hub
# Register your models here.
admin.site.register(Client)
admin.site.register(ProductImplementation)
admin.site.register(Router)
admin.site.register(Hub)
