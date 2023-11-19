from django.db import models

# Create your models here.

class User_data(models.Model):
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    reg_data = models.DateField(auto_now_add=True)
    reg_time = models.DateTimeField(auto_now_add=True, blank=True)
    agreement_check = models.BooleanField()