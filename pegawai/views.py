from django.db.models import query
import pegawai
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from pegawai.models import TambahPegawai
from .forms import *
from .filter import *

def pegawai_delete(request, pegawai_id):
    pegawai = TambahPegawai.objects.get(id=pegawai_id)
    pegawai.delete()
    return redirect('pegawai-list')

def admin_login(request):
    forms = AdminLoginForm()
    if request.method == 'POST':
        forms = AdminLoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    context = {'forms': forms}
    return render(request, 'pegawai/login.html', context)

def admin_logout(request):
    logout(request)
    return redirect('home')


def tambah_pegawai(request):
    forms = TambahPegawaiForm()
    if request.method == 'POST':
        forms = TambahPegawaiForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('tambah-pegawai')
    tambah_pegawai = TambahPegawai.objects.all()
    context = {'forms': forms, 'pegawai': tambah_pegawai}
    return render(request, 'pegawai/tambah-pegawai.html', context)

def pegawai_list(request):
    query = TambahPegawai.objects.all()
    myfilter =  PegawaiFilter(request.GET, queryset=query)
    
    tp = myfilter.qs
    context = {
        'myfilter' : myfilter,
        'pegawai': tp
        }
    return render(request, 'pegawai/pegawai-list.html', context)



def pegawai_edit(request, pegawai_id):
    pegawai = TambahPegawai.objects.get(id=pegawai_id)
    form = TambahPegawaiForm(instance=pegawai)
    if request.method == 'POST':
        form = TambahPegawaiForm(request.POST, request.FILES, instance=pegawai)       
        if form.is_valid() :
            personal_info = form.save(commit=False)
            personal_info.save()
            return redirect('pegawai-list')
    context = {
        'form': form,
    }
    return render(request, 'pegawai/pegawai-edit.html', context)

