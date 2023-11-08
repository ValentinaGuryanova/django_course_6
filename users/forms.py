from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from blogs.forms import StyleForMixin
from users.models import User

from django import forms


class UserForm(StyleForMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserProfileForm(StyleForMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'comment',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()