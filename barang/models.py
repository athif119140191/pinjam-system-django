from django.db import models
from django.core.exceptions import ValidationError
import os
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf','.doc','.docx']
    if not ext in valid_extensions:
        raise ValidationError(u'Only PDF and Word Documents can be uploaded')

class TabelBarang(models.Model):
    kode_barang = models.CharField(max_length=20)
    nama_barang = models.CharField(choices=[('Komputer', 'Komputer'), ('PC', 'PC'), ('Projector', 'Projector'), ('Mouse', 'Mouse')], max_length=100, null=True, blank=True)
    merk = models.CharField(choices=[('Asus', 'Asus'), ('Acer', 'Acer'), ('Logitech', 'Logitech'), ('Apple', 'Apple')], max_length=50)
    stok = models.IntegerField()
    kondisi = models.CharField(choices=[('Baik', 'Baik'), ('Layak', 'Layak'), ('Rusak', 'Rusak')], max_length=100)
    status = models.CharField(choices=[('Siap', 'Siap'), ('Tidak Siap', 'Tidak Siap'),], max_length=50)
    bast_perolehan = models.FileField(upload_to='barang/', validators=[validate_file_extension])

    is_delete = models.BooleanField(default=False)

    def __str__(self) :
        return str(self.kode_barang)

 

    def decrease_stok(self, count=None, save=True):
        if count == None :
            count = 0
        current_inv = self.stok
        current_inv = current_inv - int(count)
        self.stok = current_inv
        setattr(self, 'stok', self.stok)
        if save == True:
            self.save()
        return self.stok        

@receiver(post_save, sender=TabelBarang)
def nama_pre_save(sender, instance, *args, **kwargs):
    instance.decrease_stok(save=False)
