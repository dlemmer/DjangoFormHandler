from django.urls import path,re_path
from . import views

urlpatterns = [
    path('', views.form_page, name='form_page'),
    path('answer/',views.form_answer_page, name='form_answer'),
    path('edit/', views.form_answer_page, name='edit'),
    # re_path('answer/', views.delete, name='delete'),
]

