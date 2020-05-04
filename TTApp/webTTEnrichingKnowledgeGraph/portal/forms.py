from itertools import starmap
from logging import disable
from django import forms
from django.contrib.auth.management import get_default_username
from django.contrib.auth.models import User
from .models import repositoryNew, DataTurtel
 # from .models import Encuestas, Pregunta, Respuestas
from django.contrib.auth.forms import UserCreationForm
from ckeditor.widgets import CKEditorWidget
from django.utils.safestring import mark_safe
from django.db import models
from ckeditor.fields import RichTextField
from django.utils.safestring import mark_safe


class LoginFrom(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class RegisterDataFrom(forms.ModelForm):

    Type_CHOICES = (
        ('external', 'External'),
        ('local', 'Local'),
    )

    nameRepository = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    origin = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), required=True, choices=Type_CHOICES)
    state = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'value': '0', 'disabled': 'true'}), required=False)
    resource = forms.FileField(required=False)
    class Meta:
        model = repositoryNew
        fields = ['origin', 'nameRepository', 'resource', 'state']


class RegisterDataSemanticFrom(forms.ModelForm):
    DataSemantic = forms.FileField(required=False)
    nameResource = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)

    class Meta:
        model = DataTurtel
        fields = ['DataSemantic', 'nameResource']