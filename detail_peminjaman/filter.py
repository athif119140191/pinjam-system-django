import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class DetailPeminjamanFilter(django_filters.FilterSet):
	
	class Meta:
		model = DetailPeminjaman
		fields = {
			'nama_barang',
			'gedung',
			'ruang',
			}