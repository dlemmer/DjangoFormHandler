from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.utils import timezone
from FormHandler.models import User_data
from .forms import RegForm, FormEdit
from .models import User_data, User_data_edit

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
    if request.method == 'GET':
        form_edit = FormEdit()
        HttpResponse('Ваши данные успешно удалены, надеемся на ваше возвращение')
    else:
        form_edit = FormEdit(request.POST)
        if form_edit.is_valid():
            # print (form.cleaned_data)
            try:
                User_data.objects.latest('id').delete()
                User_data_edit.objects.create(**form_edit.cleaned_data)
                print(User_data_edit.objects.all())
                return HttpResponse('Ваши данные успешно изменены с:')
            except:
                form_edit.add_error(None, 'Error sending data')
    
    data = User_data.objects.latest('id')
    name = data.name
    surname = data.surname
    mail = data.email
    
    form_edit = FormEdit()
    data = {
        'name': name,
        'surname': surname,
        'mail': mail,
        "form_edit": form_edit
    }
    return render(request, './form_answer.html', data)


# def edit(request):
#     if request.method == 'POST':
#         form_edit = FormEdit()
#     else:
#         form_edit = FormEdit(request.GET)
#         if form_edit.is_valid():
#             # print (form.cleaned_data)
#             try:
#                 User_data_edit.objects.create(**form_edit.cleaned_data)
#                 print(User_data_edit.objects.all())
#                 return HttpResponse('3f3f3f')
#             except:
#                 form_edit.add_error(None, 'Error sending data')
#     return redirect(request,'./form_answer.html')


# def delete(request, pk):
#     # Retrieve the object to be deleted
#     object = User_data.objects.get(pk=pk)
#     # Delete the object
#     object.delete()
#     # Redirect to a success page or list of objects
#     return redirect('list_of_objects')