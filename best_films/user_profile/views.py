from typing import Any, Dict
from django.views.generic.base import TemplateView

# Create your views here.

PROFILE_MENU_LIST = {
    'profile_info': {'name': 'Основная информация', 'url': ''},
    'reset_pwd': {'name': 'Сброс пароля', 'url': '/auth/password-change/'},
}


class ProfileView(TemplateView):
    template_name = 'user_profile/profile.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['list_menu'] = PROFILE_MENU_LIST
        return context
