from django.db import models

# Create your models here.

class TambahGedung(models.Model):
    gedung = models.CharField(max_length=50)
    mg_gedung = models.CharField(max_length=100)
    
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.gedung
