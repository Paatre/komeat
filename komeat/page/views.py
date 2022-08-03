from typing import Optional
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views import generic


class WelcomeView(generic.TemplateView):
    template_name: str = 'page/welcome.html'


class LoginView(auth_views.LoginView):
    template_name: str = 'registration/login.html'


class IndexView(LoginRequiredMixin, generic.ListView):
    model = User
    template_name: str = 'page/index.html'
    context_object_name: Optional[str] = 'members'

    def get_queryset(self):
        return User.objects.filter(groups__name='member').order_by('first_name', 'last_name')
