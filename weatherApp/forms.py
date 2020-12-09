from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from  django import forms
from django.forms import ModelForm



#class LoginForm(AuthenticationForm):
#    username = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
#    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

class CreateUserForm(UserCreationForm):
    pass


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    username = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '', 'id': 'hello'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': '',
            'id': 'hi',
        }
    ))