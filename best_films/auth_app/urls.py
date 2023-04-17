from django.urls import path
from .views import *

urlpatterns = [
    path('reg/', RegisterUser.as_view(), name='registration'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('done', DoneUserRegistration.as_view(), name='success_url'),
]
