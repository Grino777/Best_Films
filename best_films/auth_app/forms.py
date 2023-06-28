from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext as _


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form__input', 'placeholder': 'USERNAME'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form__input', 'placeholder': 'PASSWORD'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form__input', 'placeholder': 'PASSWORD AGAIN'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form__input', 'placeholder': 'EMAIL'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')



class LoginUserForm(AuthenticationForm):
    error_messages = {
        "invalid_login": _(
            "Введен неправильный логин или пароль"
        )
    }
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form__input', 'placeholder': 'USERNAME'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form__input', 'placeholder': 'PASSWORD'}))

    class Meta:
        model = User
        error_messages = {
            "login": {
                "invalid_login": _("Введен неправильный логин или пароль"),
            }
        }
        fields = ('username', 'password')
