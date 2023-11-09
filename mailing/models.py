from django.db import models
from django.utils import timezone

from blogs.models import NULLABLE
from users.models import User


class Message(models.Model):

    theme = models.CharField(max_length=150, verbose_name='Тема сообщения')
    body = models.TextField(verbose_name='Текст сообщения')

    def __str__(self):
        return f"{self.theme}"

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = 'Сообщения'


class Mailing(models.Model):

    TITLE_CHOICES_PERIODICITY = [
        (1, 'Раз в день'),
        (2, 'Раз в неделю',),
        (3, 'Раз в месяц',),
    ]

    TITLE_CHOICES_STATUS = [
        (1, 'Создана'),
        (2, 'Запущена',),
        (3, 'Завершена',),
    ]

    mailing_time = models.DateTimeField(verbose_name="Время рассылки", default=timezone.now)
    period = models.PositiveSmallIntegerField(verbose_name="Периодичность", choices=TITLE_CHOICES_PERIODICITY, default=1)
    status = models.PositiveSmallIntegerField(verbose_name='Статус рассылки', choices=TITLE_CHOICES_STATUS, default=1)
    message = models.ForeignKey(Message, on_delete=models.SET_NULL, **NULLABLE)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f"{self.status}"

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'


class Log(models.Model):

    date_attempt = models.DateTimeField(verbose_name='Дата попытки')
    status = models.CharField(max_length=150, verbose_name='Статус попытки')
    answer = models.TextField(**NULLABLE, verbose_name='Ответ сервера')
    mailing = models.ForeignKey(Mailing, **NULLABLE, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.status} {self.date_attempt}"

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'