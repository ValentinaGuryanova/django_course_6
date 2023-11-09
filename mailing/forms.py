from django import forms

from blogs.forms import StyleFormMixin
from mailing.models import Mailing


class MailingForms(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Mailing
        fields = '__all__'