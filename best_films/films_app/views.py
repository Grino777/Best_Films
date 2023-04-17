from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

def index(request):
    return render(request, 'films_app/index.html')

class IndexView(TemplateView):
    template_name = 'films_app/index.html'