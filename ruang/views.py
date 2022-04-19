from django.shortcuts import render, redirect

from .forms import TambahRuangForm
from .models import TambahRuang
from .filter import RuangFilter

def ruang_delete(request, ruang_id):
    ruang = TambahRuang.objects.get(id=ruang_id)
    ruang.delete()
    return redirect('ruang-list')


def tambah_ruang(request):
    forms = TambahRuangForm()
    if request.method == 'POST':
        forms = TambahRuangForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('tambah-ruang')
    tambah_ruang = TambahRuang.objects.all()
    context = {'forms': forms, 'ruang': tambah_ruang}
    return render(request, 'ruang/tambah-ruang.html', context)

def ruang_list(request):
    query = TambahRuang.objects.all()
    myfilter =  RuangFilter(request.GET, queryset=query)
    
    tp = myfilter.qs
    context = {
        'myfilter' : myfilter,
        'ruang': tp
        }
    return render(request, 'ruang/ruang-list.html', context)



def ruang_edit(request, ruang_id):
    ruang = TambahRuang.objects.get(id=ruang_id)
    form = TambahRuangForm(instance=ruang)
    if request.method == 'POST':
        form = TambahRuangForm(request.POST, request.FILES, instance=ruang)       
        if form.is_valid() :
            personal_info = form.save(commit=False)
            personal_info.save()
            return redirect('ruang-list')
    context = {
        'form': form,
    }
    return render(request, 'ruang/ruang-edit.html', context)

