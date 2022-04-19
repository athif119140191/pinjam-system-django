from django.http import HttpResponse
from django.shortcuts import redirect, render

from .filter import *
from .forms import *
from .models import *


def barang_delete(request, barang_id):
    barang = TabelBarang.objects.get(id=barang_id)
    barang.delete()
    return redirect('barang-list')

# def toggle(request):
#     w = TabelBarang.objects.get(id=request.POST['id'])
#     w.is_delete = request.POST['is_delete'] == 'true'
#     w.save()
#     return HttpResponse('success')

def tambah_barang(request):
    forms = BarangForm()
    if request.method == 'POST':
        forms = BarangForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect('tambah-barang')
    tambah_barang = TabelBarang.objects.all()
    context = {'forms': forms,}
    return render(request, 'barang/tambah-barang.html', context)


def barang_list(request):
    query = TabelBarang.objects.all()
    myfilter =  TabelBarangFilter(request.GET, queryset=query)
    
    tp = myfilter.qs
    context = {
        'myfilter' : myfilter,
        'barang': tp
        }
    return render(request, 'barang/barang-list.html', context)

def barang_info(request, barang_id):
    barang = TabelBarang.objects.get(id=barang_id)
    context = {
        'barang': barang
    }
    return render(request, 'barang/barang-info.html', context)

def barang_edit(request, barang_id):
    barang = TabelBarang.objects.get(id=barang_id)
    form = BarangForm(instance=barang)
    if request.method == 'POST':
        form = BarangForm(request.POST, request.FILES, instance=barang)       
        if form.is_valid() :
            personal_info = form.save(commit=False)
            personal_info.save()
            return redirect('barang-list')
    context = {
        'form': form,
    }
    return render(request, 'barang/barang-edit.html', context)

