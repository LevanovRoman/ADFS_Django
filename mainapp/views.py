from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "mainapp/home2.html"
    context = {'title': 'Главная'}


class Login_url(TemplateView):
    template_name = "mainapp/login_url.html"
    context = {'title': 'Главная'}


class Login_no_sso_url(TemplateView):
    template_name = "mainapp/login_no_sso_url.html"
    context = {'title': 'Главная'}


class Callback_url(TemplateView):
    template_name = "mainapp/callback_url.html"
    context = {'title': 'Главная'}


class Logout_url(TemplateView):
    template_name = "mainapp/logout_url.html"
    context = {'title': 'Главная'}


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'mainapp/login_2.html'
    # success_url = 'mainapp/home_2.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login-url')


def user_data():
    ...

def user_mail():
    ...
