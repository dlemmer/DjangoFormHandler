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
                return redirect('answer/')
            except:
                form.add_error(None, 'Error sending data')
            
    data = {
        'form' : form
    }
    return render(request, './form.html', data)

def form_answer_page(request):
    # if request.method == 'POST':
    #     time_range = request.POST.get('time_range')
    #     if time_range == 'today':
    #         your_objects = User_data.objects.filter(created__date=timezone.now().date())
    #     elif time_range == 'yesterday':
    #         your_objects = User_data.objects.filter(created__date=timezone.now().date() - timezone.timedelta(days=1))
    #     elif time_range == 'this_month':
    #         your_objects = User_data.objects.filter(created__year=timezone.now().year, created__month=timezone.now().month)
    #     elif time_range == 'all_time':
    #         your_objects = User_data.objects.all()
    #     else:
    #         your_objects = User_data.objects.all()
    # else:
    #     your_objects = User_data.objects.all()
    #     return HttpResponse({'your_objects': your_objects})
        
    return render(request, './form_answer.html')
