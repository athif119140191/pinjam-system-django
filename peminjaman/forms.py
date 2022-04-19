from django import forms
from . import models
from bootstrap_datepicker_plus import DatePickerInput


class PeminjamanForm(forms.ModelForm):
    class Meta:
        model = models.Peminjaman
        exclude = {'is_delete', 'nama_pegawai'}
        widgets = {
            'no_peminjaman': forms.NumberInput(attrs={'class': 'form-control'}),
            'nip': forms.Select(attrs={'class': 'form-control'}),
            'tanggal_pinjam': DatePickerInput(format='%m/%d/%Y'),
            'tanggal_kembali': DatePickerInput(format='%m/%d/%Y'),
            'bast_disposisi': forms.ClearableFileInput(attrs={'class': 'form-control','accept': '.pdf,.doc,.docx'}),

        }
