from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('clientes/', views.clientes, name='lista_clientes'),
    path('empleados/', views.empleados, name='lista_empleados'),
    path('mesas/', views.mesas, name='lista_mesas'),
    path('platos/', views.platos, name='lista_platos'),
    path('ordenes/', views.ordenes, name='lista_ordenes'),
    path('facturas/', views.facturas, name='lista_facturas'),
]