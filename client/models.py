from django.conf import settings
from django.db import models

from blogs.models import NULLABLE


class Client(models.Model):

    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    email = models.EmailField(max_length=100, verbose_name='Почта')
    comment = models.TextField(**NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Пользователь',
                              on_delete=models.CASCADE, **NULLABLE)
    is_active = models.BooleanField(default=True, **NULLABLE, verbose_name='Активность')

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
