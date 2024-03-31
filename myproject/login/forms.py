# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    full_name = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=15, help_text='Enter your phone number.')

    class Meta:
        model = User
        fields = ['username', 'email', 'full_name', 'password1', 'password2', 'phone_number']
