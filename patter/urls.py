from django.urls import path
from . import views

urlpatterns = [
    path('', views.patter_list, name='patter_list')
]
