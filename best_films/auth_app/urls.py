from django.urls import path
from .views import (RegisterUser,
                    LoginUser,
                    logout_user,
                    DoneUserRegistration)
from .forms import LoginUserForm

urlpatterns = [
    path('reg/', RegisterUser.as_view(), name='registration'),
    path('login/', LoginUser.as_view(authentication_form=LoginUserForm), name='login', ),
    path('logout/', logout_user, name='logout'),
    path('done', DoneUserRegistration.as_view(), name='success_url'),
]
