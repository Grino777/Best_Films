from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView

from .models import Category, Movie, Status, UserMovies


# Create your views here.

CATEGORY = Category.objects.all()
STATUSES = Status.objects.all()

def add_user_movie(request, movie_id):
    # переопределить метод save для проверки записи в бд (уникальность)
    user = request.user
    movie = Movie.objects.get(id=movie_id)
    status = STATUSES.get(id=1)
    category = movie.get_category().all()
    movie_obj = UserMovies.objects.create(user=user, movie=movie, view_status=status, )
    movie_obj.category.set(category)
    movie_obj.save()
    url = request.META.get('HTTP_REFERER')
    return HttpResponseRedirect(url)


def delete_user_movie(request, obj_id):
    movie = get_object_or_404(UserMovies, movie_id=obj_id, user_id=request.user.id)
    movie.delete()
    url = request.META.get('HTTP_REFERER')
    return HttpResponseRedirect(url)


class UsersListView(ListView):
    """Вывод всех пользователей"""
    model = User
    template_name = 'films_app/users_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.order_by('username')


class CategoryFilmsView(TemplateView):
    template_name = 'films_app/user_view'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = CATEGORY
        cat_id = context['category'].get(slug=kwargs['slug']).id
        context['movies'] = Movie.objects.filter(category_id=cat_id)
        context['statuses'] = STATUSES
        return context


class AllMoviesView(ListView):
    """Вывод всех фильмов"""
    model = Movie
    template_name = 'films_app/all_movies.html'
    context_object_name = 'movies'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = CATEGORY
        context['statuses'] = STATUSES
        added_movies = UserMovies.objects.filter(user=self.request.user.id)
        context['added_movies'] = []
        for movie in added_movies:
            context['added_movies'].append(movie.movie)
        if self.kwargs:
            category = self.kwargs['slug']
            category = context['category'].get(slug=category)
            context['movies'] = context['movies'].filter(category=category)
        return context


class UserViewsView(LoginRequiredMixin, ListView):
    """Отображение фильмов пользователя"""
    model = UserMovies
    template_name = 'films_app/user_views.html'
    context_object_name = 'movies'
    login_required('auth/login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = CATEGORY
        context['statuses'] = STATUSES
        context['movies'] = UserMovies.objects.prefetch_related('movie', 'user').all()


        user = self.kwargs.get('username', self.request.user.username)
        user = User.objects.get(username=user)
        context['user'] = user.id

        category = self.kwargs.get('category_slug', 'vse')
        category = context['category'].get(slug=category)

        user_movies = context['movies'].filter(user=user.id).filter(category=category.id)
        context['user_movies'] = [movie.movie for movie in user_movies]

        query_user = context['movies'].filter(user=self.request.user)
        context['query_user'] = [movie.movie for movie in query_user]
        return context
