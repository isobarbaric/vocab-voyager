from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import VocabTerm

class WordForm(forms.Form):
    word = forms.CharField(
        label = False,
        max_length = 50,
        widget = forms.TextInput(attrs={'placeholder': 'Enter a word here'})
    )

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class VocabForm(forms.ModelForm):
    class Meta:
        model = VocabTerm
        fields = ['word']