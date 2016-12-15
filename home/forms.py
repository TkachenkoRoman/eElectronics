from django import forms
from .models import SignUpForm


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUpForm
        fields = ['email']
        widgets ={
            'email':forms.TextInput(attrs={'placeholder': 'Type your email'}),

        }



