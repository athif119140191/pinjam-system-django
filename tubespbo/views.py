from detail_peminjaman.models import DetailPeminjaman
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from peminjaman.models import Peminjaman
from pegawai.models import TambahPegawai
from barang.models import TabelBarang

@login_required(login_url='login')
def home_page(request):
    total_peminjaman = Peminjaman.objects.count()
    total_pegawai = TambahPegawai.objects.count()
    total_barang = TabelBarang.objects.count()
    total_dp = DetailPeminjaman.objects.count()
    context = {
        'barang': total_barang,
        'peminjaman': total_peminjaman,
        'pegawai': total_pegawai,
        'detail_peminjaman': total_dp,
    }
    return render(request, 'home.html', context)

