from django import forms
from . import models
from .models import *


class PlayerForm(forms.ModelForm):
    class Meta:
        model = models.Players
        exclude = ('id',)
        widgets = {}




