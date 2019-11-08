from django.shortcuts import render

# Create your views here.
def patter_list(request):
    return render(request, 'patter/patter_list.html', {})
