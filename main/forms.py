from .models import Register
from django.forms import ModelForm, TextInput
from django.contrib.auth.forms import AuthenticationForm


class RegisterForm(ModelForm):
    class Meta:
        model = Register
        fields = ['name', 'password', 'password1']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name of user'
            }),

            'password': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }),

            'password1': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Confirm password'
            })
        }