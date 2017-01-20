from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        models = Message
        fields = [
            "body",
        ]
