# Generated by Django 3.0.2 on 2020-01-28 12:31

from enum import auto
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TambahPegawai',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nip', models.CharField(max_length=20)),
                ('nama', models.CharField(max_length=100)),
                ('alamat', models.CharField(max_length=100)),
                ('telp', models.CharField(max_length=20)),
                ('role', models.CharField(choices=[('Dosen', 'Dosen'), ('Staff', 'Staff'), ('Tendik', 'Tendik'), ('Rektor', 'Rektor')], max_length=100)),
                ('is_delete', models.BooleanField(default=False)),
            ],
        ),
    ]