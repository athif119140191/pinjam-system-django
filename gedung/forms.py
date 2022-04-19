from django import forms
from . import models

class TambahGedungForm(forms.ModelForm):
    class Meta:
        model = models.TambahGedung
        exclude = {'is_delete'}
        widgets = {
            'gedung': forms.TextInput(attrs={'class': 'form-control'}),
            'mg_gedung': forms.TextInput(attrs={'class': 'form-control'}),
        }
