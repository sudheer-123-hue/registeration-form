from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Registration
        fields = ['name', 'email', 'password', 'phone', 'photo', 'resume']
