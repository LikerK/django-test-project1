from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext_lazy
from .models import User
from messager.chats.models import Chat
from .forms import UserForm
from django.shortcuts import render


# Create your views here.
class CreateUser(CreateView):
    model = User
    form_class = UserForm
    template_name = 'form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = gettext_lazy('Create')
        context['button_text'] = gettext_lazy('Registration')
        return context

class UserList(LoginRequiredMixin, ListView):
    template_name = 'users.html'
    
    def get_queryset(self):
        self.new_message = Chat.objects.filter(members__in=[self.request.user])
        return self.new_message

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = gettext_lazy('Create')
        context['new_message'] = self.new_message
        context['users'] = User.objects.all()
        return context

class NewMessage(ListView):
    template_name = 'users.html'
    model = Chat
    context_object_name = 'new_message'

    
