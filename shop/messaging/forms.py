from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = [
            "body",
        ]
        widgets = {
            'body': forms.Textarea(attrs={'rows': 1,
                                          'class': 'form-control',
                                          'placeholder': 'Type your messages....',
                                          'style': 'resize: none;'
                                          }),
        }
