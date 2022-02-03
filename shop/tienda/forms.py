from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

class ClientForm(forms.Form):
    first_name = forms.CharField(label='Nombre', max_length=200, required=True)
    last_name = forms.CharField(label='Apellido', max_length=200, required=True)
    email = forms.CharField(required=True)
    direction = forms.CharField(widget=forms.Textarea, required=True)
    phone = forms.CharField(max_length=20)
    username = forms.CharField(label='Usuario', max_length=20, required=True)
    password = forms.CharField(widget=forms.PasswordInput)


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'password']

