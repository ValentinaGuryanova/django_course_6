from django import forms

from blogs.forms import StyleForMixin
from client.models import Client


class ClientForms(StyleForMixin, forms.ModelForm):

    class Meta:
        model = Client
        fields = '__all__'