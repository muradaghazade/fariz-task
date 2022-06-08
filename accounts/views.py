from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.contrib.auth.models import User
from accounts.forms import LoginForm, RegisterForm
from django.urls import reverse_lazy

class MainLoginView(LoginView):
    template_name = 'login.html'
    form_class = LoginForm


class RegisterView(CreateView):
    model = User
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('accounts:login')
