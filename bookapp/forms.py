from .models import CustomUser
from django import forms
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.ModelForm):
    """User Login Form"""
    class Meta:
        model = CustomUser
        fields = '__all__'

class SignupForm(UserCreationForm):
    """User sign-up Form"""
    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2']
