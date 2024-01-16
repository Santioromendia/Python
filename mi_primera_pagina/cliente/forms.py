from django import forms

from . import models

class clienteForm(forms.ModelForm):
    class Meta:
        model=models.cliente
        fields = "__all__"
        
