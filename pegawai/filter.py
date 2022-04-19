import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class PegawaiFilter(django_filters.FilterSet):
	
	class Meta:
		model = TambahPegawai
		fields = {
			'nip' : ['icontains'],
			'nama'  : ['icontains'],
			'role' : ['icontains']
			}