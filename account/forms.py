from django import forms
from django.contrib.auth.models import User


class AuthenticationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]
