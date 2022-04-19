from django.urls import path

from . import views

urlpatterns = [
    path('tambah-barang', views.tambah_barang, name='tambah-barang'),
    path('barang-list', views.barang_list, name='barang-list'),
    path('info/<barang_id>', views.barang_info, name='barang-info'),
    path('delete/<barang_id>', views.barang_delete, name='barang-delete'),
    path('edit/<barang_id>', views.barang_edit, name='barang-edit'),
    # path('toggle/', views.toggle,),
]
