from django.urls import path
from . import views 


urlpatterns = [
    path('login', views.admin_login, name='login'),
    path('logout', views.admin_logout, name='logout'),
    path('tambah-pegawai', views.tambah_pegawai, name='tambah-pegawai'),
    path('pegawai-list', views.pegawai_list, name='pegawai-list'),
    path('delete/<pegawai_id>', views.pegawai_delete, name='pegawai-delete'),
    path('edit/<pegawai_id>', views.pegawai_edit, name='pegawai-edit'),
]
