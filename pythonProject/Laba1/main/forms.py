from django.contrib.auth.forms import BaseUserCreationForm
from django import forms
from .models import User, Product


class RegisterForm(BaseUserCreationForm):
    class Meta(BaseUserCreationForm.Meta):
        model = User


class NewProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('img', 'name', 'extra_info', 'price')
