from django.db import models
from gedung.models import TambahGedung

# Create your models here.

class TambahRuang(models.Model):
    ruang = models.CharField(max_length=50)
    pj_ruang = models.CharField(max_length=100)
    gedung = models.ForeignKey(TambahGedung, on_delete=models.CASCADE)
    
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.ruang