from django.db import models
from django.db.models.enums import Choices
from pegawai.models import TambahPegawai
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
import os



def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf','.doc','.docx']
    if not ext in valid_extensions:
        raise ValidationError(u'Only PDF and Word Documents can be uploaded')

class Peminjaman(models.Model):
    no_peminjaman = models.CharField(max_length=20)
    nip = models.ForeignKey(TambahPegawai, on_delete=models.CASCADE)
    nama_pegawai = models.CharField(max_length=100, null=True, blank=True)
    tanggal_pinjam = models.DateField()
    tanggal_kembali = models.DateField()
    bast_disposisi = models.FileField(upload_to='peminjaman/', validators=[validate_file_extension] , )

    is_delete = models.BooleanField(default=False)

    def __str__(self) :
        return str(self.no_peminjaman)

    def nama (self, save=False):
        if not self.nip:
            return {}
        nama_pegawai = self.nip.nama
        names ={
            'nama_pegawai' : nama_pegawai
        }
        setattr(self, 'nama_pegawai', nama_pegawai)
        if save == True:
            self.save()
        return nama_pegawai



@receiver(pre_save, sender=Peminjaman)
def nama_pre_save(sender, instance, *args, **kwargs):
    instance.nama(save=False)

#post_save.connect(nama_pre_save, sender=Peminjaman)




