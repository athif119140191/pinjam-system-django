from django.db import models


class TambahPegawai(models.Model):
    nip = models.CharField(max_length=20)
    nama = models.CharField(max_length=100)
    alamat = models.CharField(max_length=100)
    telp = models.CharField(max_length=20)
    role = models.CharField(choices=[('Dosen', 'Dosen'), ('Staff', 'Staff'), ('Tendik', 'Tendik'), ('Rektor', 'Rektor')], max_length=100)
    
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return str(self.nip)
