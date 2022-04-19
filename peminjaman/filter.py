import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class PeminjamanFilter(django_filters.FilterSet):
	
	class Meta:
		model = Peminjaman
		fields = {
			'no_peminjaman'  : ['icontains'],
			}