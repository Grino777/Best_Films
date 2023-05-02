from django.urls import path
from .views import *

urlpatterns = [
    path('', UserViewsView.as_view(), name='main'),
    path('<str:username>/movies', UserViewsView.as_view(), name='user_movies'),
    path('<str:username>/movies/category/<slug:category_slug>', UserViewsView.as_view(), name='user_movies_category'),
    # path('category/<int:category_id>', UserViewsView.as_view(), name='movies_category'),
    path('category/<slug:slug>', CategoryFilmsView.as_view(), name='category'),
    path('users', UsersListView.as_view(), name='users_list'),
    path('all_movies/<slug:slug>', AllMoviesView.as_view(), name='category_movies'),
    path('all_movies', AllMoviesView.as_view(), name='all_movies'),
    path('movie/add/<int:movie_id>', add_user_movie, name='add_movie'),
    path('movie/delete/<int:obj_id>', delete_user_movie, name='delete_movie'),
]