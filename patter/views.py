from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Patter
from .forms import PatterForm

# Create your views here.
def index(request):
    return render(request, 'patter/index.html', {})

def patter_list(request):
    patters = Patter.objects.all()

    return render(request, 'patter/patter_list.html', { 'patters' : patters })

def patter_detail(request, pk):
    patter = get_object_or_404(Patter, pk=pk)

    return render(request, 'patter/patter_detail.html', { 'patter' : patter })

def patter_new(request):
    form  = PatterForm()

    return render(request, 'patter/patter_edit.html', { 'form' : form })
