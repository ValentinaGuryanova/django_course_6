from datetime import datetime

import pytz
import smtplib
from django.conf import settings
from django.core.mail import send_mail
from django.core.management import BaseCommand

from client.models import Client
from mailing.models import Mailing, Log


class Command(BaseCommand):
    """
    Команда для отправки рассылки
    """

    def handle(self, *args, **options):
        mailings = Mailing.objects.filter(status=2)
