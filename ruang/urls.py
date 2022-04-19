from django.urls import path
from . import views

urlpatterns = [
    path('tambah-ruang', views.tambah_ruang, name='tambah-ruang'),
    path('ruang-list', views.ruang_list, name='ruang-list'),
    path('delete/<ruang_id>', views.ruang_delete, name='ruang-delete'),
    path('edit/<ruang_id>', views.ruang_edit, name='ruang-edit'),
]
