from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.utils import timezone
from FormHandler.models import User_data
from .forms import RegForm
from .models import User_data

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
                print(User_data.objects.all())
                return redirect('/answer')
            except:
                form.add_error(None, 'Error sending data')
            
    data = {
        'form' : form
    }
    return render(request, './form.html', data)

def form_answer_page(request):
    data = User_data.objects.latest('id')
    name = data.name
    surname = data.surname
    mail = data.email
    return render(request, './form_answer.html', { 'name': name,
                                                  'surname': surname,
                                                  'mail': mail})


    