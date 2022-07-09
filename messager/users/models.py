from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy


class User(AbstractUser):

    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = gettext_lazy('User')
        verbose_name_plural = gettext_lazy('Users')
        ordering = ['id']