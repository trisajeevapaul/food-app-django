from django.forms import ModelForm
from .models import Booking
from django import forms
from django.contrib.auth.forms import AuthenticationForm




class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"

class OrderForm(forms.Form):
    customer_name = forms.CharField(max_length=100)

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username',
            'autofocus': True
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        })
    )