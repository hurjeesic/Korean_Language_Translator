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
        patter = Patter(patter_str=request.POST.get('patter_str'), meaning_short_str=request.POST.get('meaning_short_str'))
        patter .save()

        return redirect('add')

    return render(request, 'patter/patter_add.html', {})

def translate(request):
    output = ''
    if request.method == "GET":
        input = request.GET.get("input");
        if input is not None:
            output = translate_func(input)


    return render(request, 'patter/translator.html', { 'input' : input, 'output' : output })

def translate_func(input):
    output = input
    patters = Patter.objects.all()
    for patter in patters:
        output = output.replace(patter.patter_str, patter.meaning_short_str)

    import os
    path = os.path.abspath('') + "/Korean_Language_Translator/patter/words/"
    file_list = os.listdir(path)
    already_word = ''
    for file_name in file_list:
        f = open(path + file_name, 'r', encoding='utf-8')
        while True:
            line = f.readline()
            if not line: break
            if len(line.split('\"')) > 2:
                data = line.split(' ')[0]
                meaning = line.split('\"')[1]
                if data != already_word:
                    already_word = data
                    output = output.replace(data, meaning)

        f.close()

    return output

def help(request):
    return render(request, 'patter/help.html', {})
