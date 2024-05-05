from django import forms

from blogs.forms import StyleFormMixin
from mailing.models import Mailing, Message


class MailingForms(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Mailing
        exclude = ['owner']


class MessageForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Message
        exclude = ("owner",)
