from django import forms
from . import models
from bootstrap_datepicker_plus import DatePickerInput


class DetailPeminjamanForm(forms.ModelForm):
    class Meta:
        model = models.DetailPeminjaman
        exclude = {'is_delete', 'nama_barang', 'status'}
        widgets = {
            'no_peminjaman': forms.Select(attrs={'class': 'form-control'}),
            'kode_barang': forms.Select(attrs={'class': 'form-control'}),
            'jumlah': forms.NumberInput(attrs={'class': 'form-control'}),
            'gedung': forms.Select(attrs={'class': 'form-control'}),
            'ruang': forms.Select(attrs={'class': 'form-control'}),

        }
