from django import forms
from django.utils import timezone
from .models import ContactMeModel


# class ContactMeForm(forms.Form):
#     name = forms.CharField(max_length=100, label='name')
#     email = forms.EmailField()
#     subject = forms.CharField(max_length=500)
#     message = forms.CharField(widget=forms.Textarea)

class ContactMeForm(forms.ModelForm):
    class Meta:
        model = ContactMeModel
        fields = ['name', 'email', 'subject', 'message']

        # alternative way (the above is the better practice):
        # fields = '__all__'
        # exclude = ('date',)


