from django.urls import path
from . import views

urlpatterns = [

    # =========================
    # AUTENTICACIÓN
    # =========================

    path('login/',
         views.login_view,
         name='login'),

    path('registro/',
         views.registro,
         name='registro'),

    path('logout/',
         views.logout_view,
         name='logout'),


    # =========================
    # INICIO
    # =========================

    path('',
         views.inicio,
         name='inicio'),


    # =========================
    # CLIENTES
    # =========================

    path('clientes/',
         views.lista_clientes,
         name='clientes'),

    path('clientes/crear/',
         views.crear_cliente,
         name='crear_cliente'),

    path('clientes/editar/<int:id>/',
         views.editar_cliente,
         name='editar_cliente'),

    path('clientes/eliminar/<int:id>/',
         views.eliminar_cliente,
         name='eliminar_cliente'),


    # =========================
    # EMPLEADOS
    # =========================

    path('empleados/',
         views.lista_empleados,
         name='empleados'),

    path('empleados/crear/',
         views.crear_empleado,
         name='crear_empleado'),

    path('empleados/editar/<int:id>/',
         views.editar_empleado,
         name='editar_empleado'),

    path('empleados/eliminar/<int:id>/',
         views.eliminar_empleado,
         name='eliminar_empleado'),


    # =========================
    # MESAS
    # =========================

    path('mesas/',
         views.lista_mesas,
         name='mesas'),

    path('mesas/crear/',
         views.crear_mesa,
         name='crear_mesa'),

    path('mesas/editar/<int:id>/',
         views.editar_mesa,
         name='editar_mesa'),

    path('mesas/eliminar/<int:id>/',
         views.eliminar_mesa,
         name='eliminar_mesa'),


    # =========================
    # PLATOS
    # =========================

    path('platos/',
         views.lista_platos,
         name='platos'),

    path('platos/crear/',
         views.crear_plato,
         name='crear_plato'),

    path('platos/editar/<int:id>/',
         views.editar_plato,
         name='editar_plato'),

    path('platos/eliminar/<int:id>/',
         views.eliminar_plato,
         name='eliminar_plato'),


    # =========================
    # ORDENES
    # =========================

    path('ordenes/',
         views.lista_ordenes,
         name='ordenes'),

    path('ordenes/crear/',
         views.crear_orden,
         name='crear_orden'),

    path('ordenes/editar/<int:id>/',
         views.editar_orden,
         name='editar_orden'),

    path('ordenes/eliminar/<int:id>/',
         views.eliminar_orden,
         name='eliminar_orden'),


    # =========================
    # FACTURAS
    # =========================

    path('facturas/',
         views.lista_facturas,
         name='facturas'),

    path('facturas/crear/',
         views.crear_factura,
         name='crear_factura'),

    path('facturas/editar/<int:id>/',
         views.editar_factura,
         name='editar_factura'),

    path('facturas/eliminar/<int:id>/',
         views.eliminar_factura,
         name='eliminar_factura'),
]