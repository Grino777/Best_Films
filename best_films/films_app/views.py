from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView

from .models import Category, Movie, Status, UserMovies


# Create your views here.

def add_user_movie(request, movie_id):
    #переопределить метод save для проверки записи в бд (уникальность)
    user = request.user
    movie = Movie.objects.get(id=movie_id)
    status = Status.objects.get(id=1)
    category = movie.get_category().all()
    movie_obj = UserMovies.objects.create(user=user, movie=movie, view_status=status, )
    movie_obj.category.set(category)
    movie_obj.save()
    url = reverse_lazy('all_movies')
    return HttpResponseRedirect(url)

def delete_user_movie(request):
    ...



class UsersListView(ListView):
    """Вывод всех пользователей"""
    model = User
    template_name = 'films_app/users_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.order_by('username')


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
        context['category'] = Category.objects.all()
        context['user_movies'] = UserMovies.objects.filter(user_id=self.request.user.id)
        context['statuses'] = Status.objects.all()
        return context

    def get_queryset(self):
        context = super(UserViewsView, self).get_queryset()
        if self.kwargs:
            category_id = self.kwargs['category_id']
            # movies = context.prefetch_related('category').get('movie')
        # context = [movie.movie_id for movie in context]
        return context
