from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Snippet, UserSettings


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(label='E-Mail')
    category = forms.ChoiceField(choices=[('question', 'Question'), ('other', 'Other')])
    subject = forms.CharField(required=False)
    body = forms.CharField(widget=forms.Textarea)


class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ('name', 'body')


class UserCreatorForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = UserSettings
        fields = ['address_one', 'address_two', 'contact_person_name', 'telephone_number']