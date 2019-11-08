from django.urls import path
from . import views

urlpatterns = [
    path('', views.patter_list, name='patter_list'),
    path('patter/<str:pk>/', views.patter_detail, name='patter_detail')
]
