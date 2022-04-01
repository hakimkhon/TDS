from dataclasses import field
from email.policy import default
from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import Lead, User

class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            "ism", "famila", "yosh", "qiziqishi", "agent", "organisation", #"tulov"
        )

class LeadForm(forms.Form):
    ism = forms.CharField(max_length=15)
    famila = forms.CharField(max_length=15)
    yosh = forms.IntegerField(min_value=8)
    qiziqishi = forms.CharField(max_length=100)
    # tulov = forms.BooleanField(default = False)

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}