from django.urls import path

from . import views

urlpatterns = [
    path('tambah-peminjaman', views.tambah_peminjaman, name='tambah-peminjaman'),
    path('peminjaman-list', views.peminjaman_list, name='peminjaman-list'),
    path('info/<peminjaman_id>', views.peminjaman_info, name='peminjaman-info'),
    path('delete/<peminjaman_id>', views.peminjaman_delete, name='peminjaman-delete'),
    path('edit/<peminjaman_id>', views.peminjaman_edit, name='peminjaman-edit'),
]
