import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class TabelBarangFilter(django_filters.FilterSet):
	
	class Meta:
		model = TabelBarang
		fields = {
			'kode_barang'  : ['icontains'],
            'nama_barang'  : ['icontains'],
			}