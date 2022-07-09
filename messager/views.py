from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy


class Index(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = gettext_lazy('Messager on Django')
        context['sub_title'] = gettext_lazy('You can login to your account or register')
        context['login'] = gettext_lazy('Login')
        context['register'] = gettext_lazy('Register')
        context['open_chat'] = gettext_lazy('Open chat')
        context['logout'] = gettext_lazy('Outlog')
        return context


class Login(LoginView):
    template_name = 'form.html'
    next_page = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = gettext_lazy('Input')
        context['button_text'] = gettext_lazy('Input')
        return context

class Logout(LogoutView):
    next_page = reverse_lazy('index')