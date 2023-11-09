from django.core.management import BaseCommand
from django.utils import timezone

from client.models import Client
from mailing.models import Mailing, Message


class Command(BaseCommand):
    """
    Команда для наполнения базы Рассылки, Клиенты, Сообщения
    """

    def handle(self, *args, **options):
        message_list = [
            {'id': 1, 'theme': 'Подарок',
             'body': 'Не упустите свой шанс получить подарок!'},
            {'id': 2, 'theme': 'Распродажа', 'body': 'Все товары со скидкой 50 %!'}
        ]
        message_for_create = []

        for message in message_list:
            message_for_create.append(
                Message(**message)
            )

        Message.objects.bulk_create(message_for_create)

        mailing_list = [
            {'mailing_time': timezone.now(), 'periodicity': 1, 'status': 1, 'message': Message.objects.get(pk=1)},
            {'mailing_time': timezone.now(), 'periodicity': 2, 'status': 2, 'message': Message.objects.get(pk=2)},
            {'mailing_time': timezone.now(), 'periodicity': 3, 'status': 1, 'message': Message.objects.get(pk=1)},
            {'mailing_time': timezone.now(), 'periodicity': 1, 'status': 3, 'message': Message.objects.get(pk=2)},
            {'mailing_time': timezone.now(), 'periodicity': 2, 'status': 1, 'message': Message.objects.get(pk=1)},
            {'mailing_time': timezone.now(), 'periodicity': 3, 'status': 3, 'message': Message.objects.get(pk=2)},
            {'mailing_time': timezone.now(), 'periodicity': 1, 'status': 1, 'message': Message.objects.get(pk=1)},
            {'mailing_time': timezone.now(), 'periodicity': 1, 'status': 3},
        ]
        mailing_for_create = []

        for mailing in mailing_list:
            mailing_for_create.append(
                Mailing(**mailing)
            )

        Mailing.objects.bulk_create(mailing_for_create)

        client_list = [
            {'first_name': 'Виктор', 'last_name': 'Иванов', 'email': 'user1@mail.ru'},
            {'first_name': 'Сергей', 'last_name': 'Лебедев', 'email': 'user2@mail.ru'},
            {'first_name': 'Андрей', 'last_name': 'Быков', 'email': 'user3@mail.ru'},
            {'first_name': 'Михаил', 'last_name': 'Ильин', 'email': 'user4@mail.ru'},
            {'first_name': 'Валентина', 'last_name': 'Мальнова', 'email': 'gvalushka@mail.ru'},
        ]
        client_for_create = []

        for client in client_list:
            client_for_create.append(
                Client(**client)
            )

        Client.objects.bulk_create(client_for_create)