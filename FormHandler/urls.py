from django.urls import path
from . import views

urlpatterns = [
    path('', views.form_page, name='form_page'),
    path('answer/' ,views.form_answer_page, name='form_answer')
]

