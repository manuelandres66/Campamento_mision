from django import forms

class Ingresar(forms.Form):
    usuario = forms.CharField(max_length=1000)
    password = forms.CharField(max_length=1000, widget=forms.PasswordInput)