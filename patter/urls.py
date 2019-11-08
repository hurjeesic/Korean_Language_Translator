from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('patter/', views.patter_list, name='patter_list'),
    path('patter/detail/<str:pk>/', views.patter_detail, name='patter_detail'),
    path('patter/new/', views.patter_new, name='patter_new')
]
