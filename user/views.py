from django.shortcuts import render
from django.views.generic import TemplateView


class LoginTestView(TemplateView):
    template_name = 'user/login.html'


class RegisterTestView(TemplateView):
    template_name = 'user/register.html'
