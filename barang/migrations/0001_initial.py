# Generated by Django 3.0.2 on 2020-01-28 12:31

from django.db import migrations, models
from barang.models import validate_file_extension

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]


    operations = [
        migrations.CreateModel(
            name='TabelBarang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_barang', models.CharField(max_length=20)),                
                ('nama_barang', models.CharField(choices=[('Komputer', 'Komputer'), ('PC', 'PC'), ('Projector', 'Projector'), ('Mouse', 'Mouse')], max_length=100, null=True, blank=True)),
                ('merk', models.CharField(choices=[('Asus', 'Asus'), ('Acer', 'Acer'), ('Logitech', 'Logitech'), ('Apple', 'Apple')], max_length=50)),
                ('stok', models.IntegerField()),
                ('kondisi', models.CharField(choices=[('Baik', 'Baik'), ('Layak', 'Layak'), ('Rusak', 'Rusak')], max_length=100)),
                ('status', models.CharField(choices=[('Siap', 'Siap'), ('Tidak Siap', 'Tidak Siap'),], max_length=50)),
                ('bast_perolehan', models.FileField(upload_to='barang/', validators=[validate_file_extension])),
                ('is_delete', models.BooleanField(default=False)),
            ],
        ),
    ]
