from django.urls import path
from .views import (CustomPasswordChangeView,
                    RegisterUser,
                    LoginUser,
                    change_password_done,
                    logout_user,
                    DoneUserRegistration)
from .forms import LoginUserForm


urlpatterns = [
    path('reg/', RegisterUser.as_view(), name='registration'),
    path('login/', LoginUser.as_view(authentication_form=LoginUserForm), name='login', ),
    path('logout/', logout_user, name='logout'),
    path('done', DoneUserRegistration.as_view(), name='success_url'),
    path('password-change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', change_password_done, name='password_change_done'),
]
