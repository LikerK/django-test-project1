from django.urls import path
from .views import CreateUser, UserList

app_name = 'users'

urlpatterns = [
    path('', UserList.as_view(), name='list'),
    path('create/', CreateUser.as_view(), name='create'),
]
