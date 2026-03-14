from django import forms
from .models import *

class PlayerForm(forms.ModelForm):
    player_firstname = forms.CharField(
        max_length=255,
        label='First Name',
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "First Name"}
        )
    )
    player_surname = forms.CharField(
        max_length=255,
        label='Last Name',
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Last Name"
        })
    )

    player_username = forms.CharField(
        max_length=12,
        label='Username',
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Username"
        })
    )

    class Meta:
        model = Players
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
        }

class CharacterForm(forms.ModelForm):

    class Meta:
        model = Characters
        fields = "__all__"
        widgets = {
            "character_name": forms.TextInput(attrs={"class": "form-control"}),
            "character_hitpoints": forms.NumberInput(attrs={"class": "form-control"}),
            "character_level": forms.NumberInput(attrs={"class": "form-control"}),
            "character_strength": forms.NumberInput(attrs={"class": "form-control"}),
            "character_intelligence": forms.NumberInput(attrs={"class": "form-control"}),
            "character_dexterity": forms.NumberInput(attrs={"class": "form-control"}),
            "character_constitution": forms.NumberInput(attrs={"class": "form-control"}),
            "character_wisdom": forms.NumberInput(attrs={"class": "form-control"}),
        }