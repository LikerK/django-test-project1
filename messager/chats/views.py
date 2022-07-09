from django.views.generic import ListView, CreateView, DeleteView
from .models import Chat, Message
from .forms import MessageForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.db.models import Count
from django.contrib import auth
from django.utils.translation import gettext_lazy


# Create your views here.
class DialogsView(View):
    def get(self, request):
        chats = Chat.objects.filter(members__in=[request.user.id])
        messages = Message.objects.all()
        return render(request, 'chats.html', {'user_profile': request.user, 'chats': chats, 'messages': messages, 'css_file': gettext_lazy('css/message.css')})


class MessagesView(CreateView):
    def get(self, request, chat_id):
        try:
            chat = Chat.objects.get(id=chat_id)
            if request.user in chat.members.all():
                chat.message_set.filter(is_readed=False).exclude(author=request.user).update(is_readed=True)
            else:
                chat = None
        except Chat.DoesNotExist:
            chat = None
 
        return render(
            request,
            'messages.html',
            {
                'user_profile': request.user,
                'chat': chat,
                'form': MessageForm(),
                'button_text': gettext_lazy('<ion-icon name="paper-plane-outline"></ion-icon>'),
                'css_file': gettext_lazy('css/message.css'),
            }
        )

    def post(self, request, chat_id):
        form = MessageForm(data=request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.chat_id = chat_id
            message.author = request.user
            message.save()
        return redirect(reverse('chats:messages', kwargs={'chat_id': chat_id}))




class CreateDialogView(View):

    def get(self, request, user_id):
        chats = Chat.objects.filter(members__in=[request.user.id, user_id], type=Chat.DIALOG).annotate(c=Count('members')).filter(c=2)
        if chats.count() == 0:
            chat = Chat.objects.create()
            chat.members.add(request.user)
            chat.members.add(user_id)
        else:
            chat = chats.first()
        return redirect(reverse('chats:messages', kwargs={'chat_id': chat.id}))


class DeleteMessages(View):

    def get(self, request, chat_id):
        Message.objects.filter(chat=chat_id).delete()
        return redirect(reverse('chats:messages', kwargs={'chat_id': chat_id}))
