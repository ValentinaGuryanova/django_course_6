from django.contrib.auth.models import AbstractUser
from django.db import models

from blogs.models import NULLABLE


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Почта')
    first_name = models.CharField(max_length=150, verbose_name='Имя', **NULLABLE)
    last_name = models.CharField(max_length=150, verbose_name='Фамилия', **NULLABLE)
    comment = models.TextField(verbose_name='Комментарий', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Фото', **NULLABLE)
    verified = models.BooleanField(default=False, verbose_name='верифицирован', blank=True)
    verified_password = models.IntegerField(verbose_name='ключ для верификации', **NULLABLE)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []




