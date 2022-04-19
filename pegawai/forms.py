from django import forms
from . import models

class AdminLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))



class TambahPegawaiForm(forms.ModelForm):
    class Meta:
        model = models.TambahPegawai
        exclude = {'is_delete'}
        widgets = {
            'nip': forms.NumberInput(attrs={'class': 'form-control'}),
            'nama': forms.TextInput(attrs={'class': 'form-control'}),
            'alamat': forms.TextInput(attrs={'class': 'form-control'}),
            'telp': forms.NumberInput(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
        }

