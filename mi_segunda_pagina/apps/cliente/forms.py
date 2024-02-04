from django import forms
from . import models

class clienteform(forms.ModelForm):
    class Meta:
        model=models.cliente
        fields="__all__"