from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User

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

    def post(self, request, *args, **kwargs):
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.instance.username = form.data['username'].lower()
            user = form.save()
            login(self.request, user)
            red_url = reverse('login')
            return HttpResponseRedirect(red_url)
        else:
            return render(request, 'auth_app/registration.html', context={'form': form})


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'auth_app/login.html'

    def get_success_url(self):
        return '/'


class DoneUserRegistration(TemplateView):
    template_name = 'auth_app/done.html'
