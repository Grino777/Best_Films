from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='main'),
    path('category/<slug:slug>', CategoryFilmsView.as_view(), name='category'),
    path('users', UsersList.as_view(), name='users_list'),
]