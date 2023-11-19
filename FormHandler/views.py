from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegForm

# Create your views here.

def form_page(request):
    if request.method == 'GET':
        form = RegForm()
    else:
        form = RegForm(request.POST)
        if form.is_valid():
            print (form.cleaned_data)
            
    data = {
        'form' : form
    }
    return render(request, 'form.html', data)
