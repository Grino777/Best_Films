from django.urls import path
from .views import AllMoviesApiView, UsersApiView

urlpatterns = [
    path('movies/', AllMoviesApiView.as_view(), name='all-movies'),
    path('users/', UsersApiView.as_view(), name='all-users'),
    
]
