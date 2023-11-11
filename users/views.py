from random import random
import random
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from users.forms import UserForm, UserRegisterForm
from users.models import User


class LoginView(BaseLoginView):
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    def form_valid(self, form):
        list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if form.is_valid():
            verified_password = ''
            for i in range(8):
                rand_idx = random.randint(0, len(list)-1)
                verified_password += str(rand_idx)

            form.verified_password = verified_password
            user = form.save()
            user.verified_password = verified_password
            send_mail(
                subject='Поздравляем с регистрацией!',
                message=f'Подтвердите вашу регистрацию, нажмите на ссылку: http://127.0.0.1:8000/users/verifying?code={user.verified_password}\n ',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email]
            )
            return super().form_valid(form)


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user