from django import forms # type: ignore
from django.contrib.auth.forms import User, UserCreationForm, AuthenticationForm # type: ignore
from django.forms.widgets import PasswordInput, TextInput


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        
        first_name = forms.CharField(widget=forms.TextInput())
        last_name = forms.CharField(widget=forms.TextInput())
        username = forms.CharField(widget=forms.TextInput())
        email = forms.CharField(widget=forms.EmailField())
        password1 = forms.CharField(widget=forms.PasswordInput())
        password2 = forms.CharField(widget=forms.PasswordInput())



class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    

    