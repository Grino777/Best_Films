from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from .forms import *

# Create your views here.
from django.views.generic import TemplateView, CreateView


def logout_user(request):
    logout(request)
    return redirect('/')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'auth_app/registration.html'
    success_url = reverse_lazy('success_url')

    def form_valid(self, form):
        '''Метод автоматической авторизации пользователя при регистрации'''
        user = form.save()
        login(self.request, user)
        return reverse_lazy('success_url')

    def post(self, request, *args, **kwargs):
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            self.form_valid(form)
        else:
            return render(request, 'auth_app/registration.html', context={'form': form})


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'auth_app/login.html'

    def get_success_url(self):
        return '/'


class DoneUserRegistration(TemplateView):
    template_name = 'auth_app/done.html'
