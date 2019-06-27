from django.urls import path
from . import views

urlpatterns = [
	path('', views.createForm),
    path('create/', views.createForm),
    path('view/', views.viewData),
    path('index/', views.index),
    path('fetchData/', views.fetchData),
]