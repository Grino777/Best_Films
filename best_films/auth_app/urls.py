from django.urls import path
from .views import *

urlpatterns = [
    path('reg/', RegisterUser.as_view()),
    path('login/', LoginUser.as_view()),
    path('done', DoneUserRegistration.as_view())
]
