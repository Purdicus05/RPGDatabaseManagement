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
    character_name = forms.CharField(
        max_length=255,
        label='Name',
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Name"
        })
    )
    character_class = forms.CharField(
        max_length=255,
        label='Class',
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Class"
        })
    )
    character_race = forms.CharField(
        max_length=255,
        label='Race',
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Race"
        })
    )
    character_armor = forms.ModelChoiceField(
        queryset=Armour.objects.all(),
        empty_label="Select Armour",
        label='Armour',
        required=True,
        widget=forms.Select(attrs={
            "class": "form-control",
            "aria-label": "Select Armour"
        })
    )
    character_weapon = forms.ModelChoiceField(
        queryset=Weapons.objects.all(),
        empty_label="Select Weapon",
        label='Weapon',
        required=False,
        widget=forms.Select(attrs={
            "class": "form-control",
            "aria-label": "Select Weapon"
        })
    )
    character_spell = forms.ModelChoiceField(
        queryset=Spells.objects.all(),
        empty_label="Select Spell",
        label='Spell',
        required=False,
        widget=forms.Select(attrs={
            "class": "form-control",
            "aria-label": "Select Spell"
        })
    )
    character_hp = forms.IntegerField(
        label='HP',
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "HP"
        })
    )
    character_level = forms.IntegerField(
        label='Level',
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Level"
        })
    )
    character_strength = forms.IntegerField(
        label='Strength',
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Strength"
        })
    )
    character_intelligence = forms.IntegerField(
        label='Intelligence',
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Intelligence"
        })
    )
    character_dexterity = forms.IntegerField(
        label='Dexterity',
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Dexterity"
        })
    )
    character_constitution = forms.IntegerField(
        label='Constitution',
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Constitution"
        })
    )
    character_wisdom = forms.IntegerField(
        label='Wisdom',
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Wisdom"
        })
    )
    character_player = forms.ModelChoiceField(
        queryset=Players.objects.all(),
        empty_label="Select Player",
        required=True,
        widget=forms.Select(attrs={
            "class": "form-control",
            "aria-label": "Select Player"
        })
    )