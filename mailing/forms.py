from django import forms

from blogs.forms import StyleForMixin
from mailing.models import Mailing


class MailingForms(StyleForMixin, forms.ModelForm):

    class Meta:
        model = Mailing
        fields = '__all__'