from pegawai.models import TambahPegawai
from django.shortcuts import render, redirect

from .forms import PeminjamanForm
from .models import Peminjaman
from .filter import PeminjamanFilter

def peminjaman_delete(request, peminjaman_id):
    peminjaman = Peminjaman.objects.get(id=peminjaman_id)
    peminjaman.delete()
    return redirect('peminjaman-list')


def tambah_peminjaman(request):
    forms = PeminjamanForm()
    if request.method == 'POST':
        forms = PeminjamanForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect('tambah-peminjaman')
    tambah_peminjaman = Peminjaman.objects.all()
    context = {'forms': forms,}
    return render(request, 'peminjaman/tambah-peminjaman.html', context)


def peminjaman_list(request):
    query = Peminjaman.objects.all()
    myfilter =  PeminjamanFilter(request.GET, queryset=query)
    
    tp = myfilter.qs
    context = {
        'myfilter' : myfilter,
        'peminjaman': tp
        }
    return render(request, 'peminjaman/peminjaman-list.html', context)

def peminjaman_info(request, peminjaman_id):
    peminjaman = Peminjaman.objects.get(id=peminjaman_id)
    context = {
        'peminjaman': peminjaman
    }
    return render(request, 'peminjaman/peminjaman-info.html', context)

def peminjaman_edit(request, peminjaman_id):
    peminjaman = Peminjaman.objects.get(id=peminjaman_id)
    form = PeminjamanForm(instance=peminjaman)
    if request.method == 'POST':
        form = PeminjamanForm(request.POST, request.FILES, instance=peminjaman)       
        if form.is_valid() :
            personal_info = form.save(commit=False)
            personal_info.save()
            return redirect('peminjaman-list')
    context = {
        'form': form,
    }
    return render(request, 'peminjaman/peminjaman-edit.html', context)

