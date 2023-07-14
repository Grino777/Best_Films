from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.forms import ValidationError


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={"class": "form__input", "placeholder": "USERNAME"}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"class": "form__input", "placeholder": "PASSWORD"}))
    password2 = forms.CharField(label="Повтор пароля", widget=forms.PasswordInput(attrs={"class": "form__input", "placeholder": "PASSWORD AGAIN"}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={"class": "form__input", "placeholder": "EMAIL"}))

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")


class LoginUserForm(AuthenticationForm):
    error_messages = {"invalid_login": _("Введен неправильный логин или пароль")}
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={"class": "form__input", "placeholder": "USERNAME"}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"class": "form__input", "placeholder": "PASSWORD"}))

    class Meta:
        model = User
        error_messages = {
            "login": {
                "invalid_login": _("Введен неправильный логин или пароль"),
            }
        }
        fields = ("username", "password")


class PasswordForm(forms.Form):
    current_password = forms.CharField(label="Старый пароль", widget=forms.PasswordInput(attrs={"class": "form__input password2", "placeholder": "CURRENT PASSWORD"}), required=False)
    password = forms.CharField(label="Новый пароль", widget=forms.PasswordInput(attrs={"class": "form__input password", "placeholder": "PASSWORD"}), required=False, )
    confirm_password = forms.CharField(label="Подтверждение пароля", widget=forms.PasswordInput(attrs={"class": "form__input password1", "placeholder": "CONFIRM PASSWORD"}), required=False)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(PasswordForm, self).__init__(*args, **kwargs)
