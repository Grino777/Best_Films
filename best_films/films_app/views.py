from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import TemplateView, ListView

from .models import Category, Movie, Status, UserMovies


# Create your views here.

def add_user_movie(request, movie_id):
    user = request.user
    movie = Movie.objects.get(id=movie_id)
    movie = UserMovies.objects.create(user_id=user, movie_id=movie)
    movie.save()

def delete_user_movie(request):
    ...


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'films_app/index.html'
    login_required('auth/login')

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


class AllMoviesView(ListView):
    """Вывод всех фильмов"""
    model = Movie
    template_name = 'films_app/all_movies.html'
    context_object_name = 'movies'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['statuses'] = Status.objects.all()
        if self.kwargs:
            category = self.kwargs['slug']
            category = context['category'].filter(slug=category)[0]
            context['movies'] = context['movies'].filter(category=category)
        return context


class UserViewsView(LoginRequiredMixin, ListView):
    """Отображение фильмов пользователя"""
    model = UserMovies
    template_name = 'films_app/all_movies.html'
    context_object_name = 'movies'
    login_required('auth/login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
