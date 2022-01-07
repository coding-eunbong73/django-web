from django import forms
from django.forms import fields
from .models import Sale
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model
User = get_user_model()

class SaleModelForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = (
            'first_name', 
            'last_name',
            'age',
            'person',
        )

class SaleForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)

class OurUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}