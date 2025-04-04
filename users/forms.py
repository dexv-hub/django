from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import User
from django import forms

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form__input', 'placeholder': 'Username'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : 'form__input', 'placeholder' : 'Password'
    }))

    class Meta:
        model = User
        fields = ['username', 'password']

class RegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg', 'placeholder': 'Username'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control form-control-lg', 'placeholder': 'Email'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-lg', 'placeholder': 'Password'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-lg', 'placeholder': 'Confirm your password'
    }))


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'small mb-1', 'readonly' : True
    }))

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'small mb-1'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'small mb-1'
    }))

    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'small mb-1', 'readonly' : True
    }))

    birthday = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'small mb-1'
    }))

    country = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'small mb-1'

    }))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'country', 'birthday']