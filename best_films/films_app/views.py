from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import TemplateView, ListView


# Create your views here.

def index(request):
    return render(request, 'films_app/index.html')

class IndexView(TemplateView):
    template_name = 'films_app/index.html'

class UsersList(ListView):
    model = User
    template_name = 'films_app/users_list.html'
    context_object_name = 'users'
