from django.contrib.auth.forms import BaseUserCreationForm

from .models import User


class RegisterForm(BaseUserCreationForm):
    class Meta(BaseUserCreationForm.Meta):
        model = User


