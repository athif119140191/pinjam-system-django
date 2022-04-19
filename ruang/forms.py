from django import forms
from . import models

class TambahRuangForm(forms.ModelForm):
    class Meta:
        model = models.TambahRuang
        exclude = {'is_delete'}
        widgets = {
            'ruang': forms.TextInput(attrs={'class': 'form-control'}),
            'pj_ruang': forms.TextInput(attrs={'class': 'form-control'}),
            'gedung': forms.Select(attrs={'class': 'form-control'}),
        }
