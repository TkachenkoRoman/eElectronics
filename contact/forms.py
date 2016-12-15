from django import forms
from .models import ContactForm


class ContactForm(forms.ModelForm):
    cc_myself = forms.BooleanField(required=False)

    class Meta:
        model = ContactForm
        fields = ['subject', 'sender', 'message' ]



