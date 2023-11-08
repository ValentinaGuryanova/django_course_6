from django.contrib.auth.models import Group
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView

from django.urls import reverse_lazy

from django.views.generic import CreateView, UpdateView

from users.forms import UserForm, UserProfileForm
from users.models import User


class LoginView(BaseLoginView):
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    pass


class RegisterUserView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        if form.is_valid():
            my_group = Group.objects.get(name='manager_mailing')
            my_group.user_set.add(user)

        return super().form_valid(form)


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile_info')

    def get_object(self, queryset=None):
        return self.request.user
