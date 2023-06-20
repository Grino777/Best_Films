from django.urls import path
from .views import *

urlpatterns = [
    path('movies/<slug:category_slug>/', AllMoviesView.as_view(), name='category_all_movies'),
    path('<str:username>/movies/<slug:category_slug>/', UserViewsView.as_view(), name='user_category_movies'),
    path('<str:username>/movies/<slug:slug>/<str:status>/', UserViewsView.as_view(), name='user_status_filter'),
    path('movie/add/<slug:movie_slug>/', add_user_movie, name='add_movie'),
    path('movie/delete/<slug:movie_slug>/', delete_user_movie, name='delete_movie'),
    path('users', UsersListView.as_view(), name='users_list'),
]
