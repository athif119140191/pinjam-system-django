from django.urls import path

from . import views

urlpatterns = [
    path('tambah-dp', views.tambah_dp, name='tambah-dp'),
    path('dp-list', views.dp_list, name='dp-list'),
    path('delete/<dp_id>', views.dp_delete, name='dp-delete'),
    path('edit/<dp_id>', views.dp_edit, name='dp-edit'),
]
