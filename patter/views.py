from django.shortcuts import render
from django.utils import timezone
from .models import Patter

# Create your views here.
def patter_list(request):
    patters = Patter.objects.all()
    return render(request, 'patter/patter_list.html', {'patters' : patters})
