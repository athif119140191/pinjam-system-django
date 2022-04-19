from django.shortcuts import render, redirect

from .forms import TambahGedungForm
from .models import TambahGedung
from .filter import GedungFilter

def gedung_delete(request, gedung_id):
    gedung = TambahGedung.objects.get(id=gedung_id)
    gedung.delete()
    return redirect('gedung-list')


def tambah_gedung(request):
    forms = TambahGedungForm()
    if request.method == 'POST':
        forms = TambahGedungForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('tambah-gedung')
    tambah_gedung = TambahGedung.objects.all()
    context = {'forms': forms, 'gedung': tambah_gedung}
    return render(request, 'gedung/tambah-gedung.html', context)

def gedung_list(request):
    query = TambahGedung.objects.all()
    myfilter =  GedungFilter(request.GET, queryset=query)
    
    tp = myfilter.qs
    context = {
        'myfilter' : myfilter,
        'gedung': tp
        }
    return render(request, 'gedung/gedung-list.html', context)



def gedung_edit(request, gedung_id):
    gedung = TambahGedung.objects.get(id=gedung_id)
    form = TambahGedungForm(instance=gedung)
    if request.method == 'POST':
        form = TambahGedungForm(request.POST, request.FILES, instance=gedung)       
        if form.is_valid() :
            personal_info = form.save(commit=False)
            personal_info.save()
            return redirect('gedung-list')
    context = {
        'form': form,
    }
    return render(request, 'gedung/gedung-edit.html', context)

