from django.shortcuts import render
from django.http import HttpResponse

from FormHandler.models import User_data
from .forms import RegForm

# Create your views here.

def form_page(request):
    if request.method == 'GET':
        form = RegForm()
    else:
        form = RegForm(request.POST)
        if form.is_valid():
            # print (form.cleaned_data)
            try:
                User_data.objects.create(**form.cleaned_data)
            except:
                form.add_error(None, 'Error sending data')
            
    data = {
        'form' : form
    }
    return render(request, 'form.html', data)
