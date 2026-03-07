from django import forms
from .models import Players

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Players
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "level": forms.NumberInput(attrs={"class": "form-control"}),
        }
