import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class RuangFilter(django_filters.FilterSet):
	
	class Meta:
		model = TambahRuang
		fields = {
			'ruang'  : ['icontains'],
			'pj_ruang' : ['icontains'],
			}