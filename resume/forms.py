from django import forms
from django.utils import timezone
from .models import ContactMeModel


class ContactMeForm(forms.ModelForm):
    class Meta:
        model = ContactMeModel
        # exclude = ['author', 'updated', 'created', ]

        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'id': 'post-name',
                'required': True,
                'placeholder': 'Name...'
            }),
            'email': forms.EmailInput(attrs={
                'id': 'post-email',
                'required': True,
                'placeholder': 'Email...'
            }),
            'subject': forms.TextInput(attrs={
                'id': 'post-subject',
                'required': True,
                'placeholder': 'Subject...'
            }),
            'message': forms.Textarea(attrs={
                'id': 'post-message',
                'required': True,
                'cols': 40,
                'rows': 10,
                'placeholder': 'Type a message here...',
            })
            }
