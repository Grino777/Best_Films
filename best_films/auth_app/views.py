from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .forms import *

# Create your views here.
from django.views.generic import TemplateView


class UserRegistration(View):
    def get(self, request, *args, **kwargs):
        form = UserRegistrationForm(request.POST)
        return render(request, 'auth_app/registration.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
        else:
            return render(request, 'auth_app/registration', context={'form': form})
        return HttpResponseRedirect('done')



class DoneUserRegistration(TemplateView):
    template_name = 'auth_app/done.html'
