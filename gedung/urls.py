from django.urls import path

from . import views

urlpatterns = [
    path('tambah-gedung', views.tambah_gedung, name='tambah-gedung'),
    path('gedung-list', views.gedung_list, name='gedung-list'),
    path('delete/<gedung_id>', views.gedung_delete, name='gedung-delete'),
    path('edit/<gedung_id>', views.gedung_edit, name='gedung-edit'),
]
