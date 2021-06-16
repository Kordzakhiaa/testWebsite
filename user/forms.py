from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import UserCreationForm

from django import forms
from user.models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        # model = get_user_model()
        model = CustomUser
        fields = ['email', 'password1', 'password2']
