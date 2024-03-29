from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy


from .forms import RegisterUserForm, AuthenticationForm
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import PasswordChangeView

# Create your views here.

def change_password_done(request):
    return render(request, 'auth_app/reset_password_done.html')

def logout_user(request):
    logout(request)
    return redirect("login")


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = "auth_app/registration.html"
    success_url = reverse_lazy("success_url")

    def post(self, request, *args, **kwargs):
        """Метод для post-запроса с измененной регистрацией (без учета регистра)."""
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.instance.username = form.data["username"].lower()
            user = form.save()
            login(self.request, user)
            red_url = reverse_lazy("user_category_movies", kwargs={"username": self.request.user.username, "category_slug": "vse"})  # type: ignore
            return HttpResponseRedirect(red_url)
        else:
            return render(request, "auth_app/registration.html", context={"form": form})


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = "auth_app/login.html"

    def post(self, request: HttpRequest, *args, **kwargs):
        """Метод для post-запроса с измененной авторизацией (без учета регистра)."""
        username = request.POST["username"].lower()
        user = request.POST.copy()
        user["username"] = username
        request.POST = user
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy("user_category_movies", kwargs={"username": self.request.user.username, "category_slug": "vse"})  # type: ignore


class DoneUserRegistration(TemplateView):
    template_name = "auth_app/done.html"


class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'auth_app/reset_password.html'
    success_url = reverse_lazy('password_change_done')
