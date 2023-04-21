from django.contrib.auth.models import User
from django.views.generic import TemplateView, ListView

from .models import Category, Movie, Status


# Create your views here.
class IndexView(TemplateView):
    template_name = 'films_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context

class CategoryFilmsView(TemplateView):
    template_name = 'films_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        cat_id = context['category'].get(slug=kwargs['slug']).id
        context['movies'] = Movie.objects.filter(category_id=cat_id)
        context['statuses'] = Status.objects.all()
        return context


class UsersList(ListView):
    model = User
    template_name = 'films_app/users_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        context = super().get_queryset()
        context = User.objects.order_by('username')
        return context
