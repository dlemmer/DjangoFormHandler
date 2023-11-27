from django import forms

class RegForm(forms.Form):
    name = forms.CharField(max_length=15, label="Name")
    surname = forms.CharField(max_length=15, label="Surname")
    email = forms.EmailField(max_length=50, label="Email")
    agreement_check = forms.BooleanField(initial=False, label="Agreement")


class FormEdit(forms.Form):
    name1 = forms.CharField(max_length=15,label="Name")
    surname1 = forms.CharField(max_length=15,label="Surname")
    email1 = forms.EmailField(max_length=50,label="Email")