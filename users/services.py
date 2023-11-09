from random import random
import random

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.exceptions import BadRequest
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse

from users.models import User


@login_required
def generate_new_password(request):

    new_password = ''.join([str(random.randint(0,9)) for _ in range(12)])
    send_mail(
        subject='Вы сменили пароль',
        message=f'Ваш новый пароль: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('blogs:main'))


# def generate_verified_code():
#     return random.choice('0123456789')


def verify_view(request):
    try:
        code = int(request.GET.get('code'))
        user = User.objects.get(verified_password=code)
    except (TypeError, User.DoesNotExists):
        raise BadRequest('Failed to verify code.')
    else:
        user.verified = True
        user.save()
    return render(request, 'users/verifying.html')