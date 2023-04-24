from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='main'),
    path('category/<slug:slug>', CategoryFilmsView.as_view(), name='category'),
    path('users', UsersList.as_view(), name='users_list'),
    path('all_movies/<slug:slug>', AllMoviesView.as_view(), name='category_movies'),
    path('all_movies', AllMoviesView.as_view(), name='all_movies'),

]