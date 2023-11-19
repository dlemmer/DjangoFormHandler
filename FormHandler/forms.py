from django import forms

class RegForm(forms.Form):
    Name = forms.CharField(max_length=15)
    Surname = forms.CharField(max_length=15)
    Email = forms.EmailField(max_length=50)
    Agreement_check = forms.BooleanField()