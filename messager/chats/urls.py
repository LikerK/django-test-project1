from django.urls import path
from .views import DialogsView, CreateDialogView, MessagesView, DeleteMessages

app_name = 'chats'

urlpatterns = [
    path('', DialogsView.as_view(), name='list'),
    path('create/<int:user_id>/', CreateDialogView.as_view(), name='create'),
    path('<int:chat_id>/', MessagesView.as_view(), name='messages'),
    path('<int:chat_id>/delete/', DeleteMessages.as_view(), name='delete'),
]
