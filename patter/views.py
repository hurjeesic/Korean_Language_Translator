from django.shortcuts import render, get_object_or_404, redirect
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
    if request.method == "POST":
        form = PatterForm(request.POST)
        if form.is_valid():
            patter = form.save(commit=False)
            # patter.author = request.user
            patter.save()

            return redirect('patter_detail', pk=patter.pk)
    else:
        form = PatterForm()

    return render(request, 'patter/patter_edit.html', { 'form' : form })

def patter_edit(request, pk):
    patter = get_object_or_404(Patter, pk=pk)
    if request.method == "POST":
        form = PatterForm(request.POST, instance=patter)
        if form.is_valid():
            patter = form.save(commit=False)
            patter.author = request.user
            patter.save()

            return redirect('patter_detail', pk=patter.pk)
    else:
        form = PatterForm(instance=patter)

    return render(request, 'patter/patter_edit.html', { 'form' : form })

def patter_delete(request, pk):
    patter = get_object_or_404(Patter, pk=pk)

    patter.delete()

    return redirect('patter_list')

def patter_add(request):
    if request.method == "POST":
        return redirect('index')

    return render(request, 'patter/patter_add.html', {})

def translate(request):
    if request.method == "POST":
        return redirect('translate')

    return render(request, 'patter/translator.html', {})

def help(request):    
    return render(request, 'patter/help.html', {})
