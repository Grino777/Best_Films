from django import forms
from django.contrib.auth.models import User


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        password = forms.CharField(widget=forms.PasswordInput())
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')

