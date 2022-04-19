import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class GedungFilter(django_filters.FilterSet):
	
	class Meta:
		model = TambahGedung
		fields = {
			'gedung'  : ['icontains'],
			'mg_gedung' : ['icontains']
			}