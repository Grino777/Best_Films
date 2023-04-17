from django.urls import path
from .views import *

urlpatterns = [
    # path('', IndexView.as_view(), name='main'),
    path('', index, name='main'),
]