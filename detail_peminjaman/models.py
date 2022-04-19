from decimal import Decimal
from django.db import models
from django.db.models.enums import Choices
from peminjaman.models import Peminjaman
from barang.models import TabelBarang
from gedung.models import TambahGedung
from ruang.models import TambahRuang
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver


class DetailPeminjaman(models.Model):
    no_peminjaman = models.ForeignKey(Peminjaman, on_delete=models.CASCADE)
    kode_barang = models.ForeignKey(TabelBarang, on_delete=models.CASCADE)
    nama_barang = models.CharField(max_length=100, null=True, blank=True)
    jumlah = models.IntegerField()
    status = models.CharField(choices=[('Siap', 'Siap'), ('Tidak Siap', 'Tidak Siap'),], max_length=50)
    gedung = models.ForeignKey(TambahGedung, on_delete=models.CASCADE)
    ruang = models.ForeignKey(TambahRuang, on_delete=models.CASCADE)

    is_delete = models.BooleanField(default=False)

    

    def __str__(self):
        return str(self.nama_barang)

    def jumlah_stok(self, save=False):
        jumlah_obj = self.jumlah
        count = getattr(self, 'jumlah', jumlah_obj)
        self.kode_barang.decrease_stok(count, save=True)
        return jumlah_obj

    def nama (self, save=False):
        if not self.kode_barang:
            return {}
        nama_barang = self.kode_barang.nama_barang
        status = self.kode_barang.status
        content = {
            'nama_barang' : nama_barang,
            'status' : status,
        }
        for k,v in content.items():
            setattr(self, k,v)
            if save == True:
                self.save()
        return content

@receiver(pre_save, sender=DetailPeminjaman)
def nama_pre_save(sender, instance, *args, **kwargs):
    instance.nama(save=False)
    

#post_save.connect(nama_pre_save, sender=Peminjaman)
@receiver(post_save, sender=DetailPeminjaman)
def nama_post_save(sender, instance, *args, **kwargs):
    instance.jumlah_stok(save=False)

