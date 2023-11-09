from django import forms

from blogs.forms import StyleFormMixin
from client.models import Client


class ClientForms(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Client
        fields = '__all__'