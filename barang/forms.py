from django import forms
from django.forms import widgets
from . import models

class BarangForm(forms.ModelForm):
    class Meta:
        model = models.TabelBarang
        exclude = {'is_delete',}
        widgets = {
            'kode_barang': forms.NumberInput(attrs={'class': 'form-control'}),
            'nama_barang': forms.Select(attrs={'class': 'form-control'}),
            'merk': forms.Select(attrs={'class': 'form-control'}),
            'stok': forms.NumberInput(attrs={'class': 'form-control'}),
            'kondisi': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'bast_perolehan': forms.ClearableFileInput(attrs={'class': 'form-control','accept': '.pdf,.doc,.docx'}),

        }

