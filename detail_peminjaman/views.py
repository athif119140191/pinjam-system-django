
from django.shortcuts import render, redirect

from .forms import DetailPeminjamanForm
from .models import DetailPeminjaman
from .filter import DetailPeminjamanFilter

from barang.models import TabelBarang

def dp_delete(request, dp_id):
    dp = DetailPeminjaman.objects.get(id=dp_id)
    dp.delete()
    return redirect('dp-list')


def tambah_dp(request):
    forms = DetailPeminjamanForm()
    if request.method == 'POST':
        #barang_id = request.session.get('TabelBarang_id')
        #barang_obj = TabelBarang.objects.get(id=barang_id)
        #jumlah_id = request.session.get("DetailPeminjaman_id")
        #jumlah_obj = DetailPeminjaman.objects.get(id=jumlah_id)
        #if jumlah_id == None:
        #    new_creation = True
        #    jumlah_obj = DetailPeminjaman.objects.create(kode_barang=barang_obj)
        #if jumlah_obj != None and new_creation == False:
        #    if jumlah_obj.barang_id != barang_id:
        #        jumlah_obj = DetailPeminjaman.objects.create(kode_barang=barang_obj)
        #request.session['DetailPeminjaman_id'] = jumlah_obj.id
        forms = DetailPeminjamanForm(request.POST, request.FILES)
        if forms.is_valid():
            #data = forms.cleaned_data.get("jumlah")
            #jumlah_obj.jumlah_stok(count=data, save=True)                        
            forms.save()
            return redirect('tambah-dp')
    tambah_dp = DetailPeminjaman.objects.all()
    context = {'forms': forms,}
    return render(request, 'detail_peminjaman/tambah-dp.html', context)


def dp_list(request):
    query = DetailPeminjaman.objects.all()
    myfilter =  DetailPeminjamanFilter(request.GET, queryset=query)
    
    tp = myfilter.qs
    context = {
        'myfilter' : myfilter,
        'dp': tp
        }
    return render(request, 'detail_peminjaman/dp-list.html', context)


def dp_edit(request, dp_id):
    dp = DetailPeminjaman.objects.get(id=dp_id)
    form = DetailPeminjamanForm(instance=dp)
    if request.method == 'POST':
        form = DetailPeminjamanForm(request.POST, request.FILES, instance=dp)       
        if form.is_valid() :
            personal_info = form.save(commit=False)
            personal_info.save()
            return redirect('dp-list')
    context = {
        'form': form,
    }
    return render(request, 'detail_peminjaman/dp-edit.html', context)

