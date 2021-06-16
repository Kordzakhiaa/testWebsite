from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView, LogoutView

from user.forms import CustomUserCreationForm


class LoginTestView(LoginView):
    template_name = 'user/login.html'


class LogoutTestView(LogoutView):
    pass


class RegisterTestView(CreateView):
    template_name = 'user/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('user:login-view')
