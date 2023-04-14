from django.urls import path
from .views import *

urlpatterns = [
    path('reg', UserRegistration.as_view()),
    path('done', DoneUserRegistration.as_view())
]