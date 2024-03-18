from django.urls import path
from .views import *

urlpatterns = [
    path('store/add', add_store, name='add_store'),
    path('store/edit/<int:id>', edit_store, name='edit_store'),
    path('store/delete/<int:id>', delete_store, name='delete_store'),
    path('store/list', list_store, name='list_store'),
    
    path('giftvoucher/add', add_giftvoucher, name='add_giftvoucher'),
    path('giftvoucher/edit/<int:id>', edit_giftvoucher, name='edit_giftvoucher'),
    path('giftvoucher/delete/<int:id>', delete_giftvoucher, name='delete_giftvoucher'),
    path('giftvoucher/list', list_giftvoucher, name='list_giftvoucher'),
    
    
    path('barcode/add', add_barcode, name='add_barcode'),
    path('barcode/edit/<int:id>', edit_barcode, name='edit_barcode'),
    path('barcode/delete/<int:id>', delete_barcode, name='delete_barcode'),
    path('barcode/used/<int:id>', use_barcode, name='use_barcode'),
    path('barcode/list', list_barcode, name='list_barcode'),
    path('barcode/dashboard', dashboard_barcode, name='dashboard_barcode'),
    path('barcode/activities', activities_barcode, name='activities_barcode'),

]