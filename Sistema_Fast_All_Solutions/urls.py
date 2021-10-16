"""FastAllSolutionsG URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('ruta1', views.miprimerafuncion),
    #path('ruta2', views.misegundafuncion),



##-------ruta para entidad cargo-----##
    path('consultar_cargo/', views.consultar_cargo,name='consultar_cargo'),
    path('crear_cargo/', views.crear_cargo,name='crear_cargo'),
    path('eliminar_cargo/<int:id>', views.eliminar_cargo,name='eliminar_cargo'),
    path('modificar_cargo/<int:id>', views.modificar_cargo,name='modificar_cargo'),




##-------ruta para entidad categoria-----##
    path('consultar_categoria/', views.consultar_categoria,name='consultar_categoria'),
    path('crear_categoria/', views.crear_categoria,name='crear_categoria'),
    path('eliminar_categoria/<int:id>', views.eliminar_categoria,name='eliminar_categoria'),
    path('modificar_categoria/<int:id>', views.modificar_categoria,name='modificar_categoria'),



##-------ruta para entidad ciudad-----##
    path('consultar_ciudad/', views.consultar_ciudad,name='consultar_ciudad'),
    path('crear_ciudad/', views.crear_ciudad,name='crear_ciudad'),
    path('eliminar_ciudad/<int:id>', views.eliminar_ciudad,name='eliminar_ciudad'),
    path('modificar_ciudad/<int:id>', views.modificar_ciudad,name='modificar_ciudad'),



##-------ruta para entidad cliente-----##
    path('consultar_cliente/', views.consultar_cliente,name='consultar_cliente'),
    path('crear_cliente/', views.crear_cliente,name='crear_cliente'),
    path('eliminar_cliente/<int:id>', views.eliminar_cliente,name='eliminar_cliente'),
    path('modificar_cliente/<int:id>', views.modificar_cliente,name='modificar_cliente'),



##-------ruta para entidad detalle_factura-----##
    path('consultar_detalle_factura/', views.consultar_detalle_factura,name='consultar_detalle_factura'),
    path('crear_detalle_factura/', views.crear_detalle_factura,name='crear_detalle_factura'),
    path('eliminar_detalle_factura/<int:id>', views.eliminar_detalle_factura,name='eliminar_detalle_factura'),
    path('modificar_detalle_factura/<int:id>', views.modificar_detalle_factura,name='modificar_detalle_factura'),



##-------ruta para entidad detalle_mantenimiento-----##
    path('consultar_detalle_mantenimiento/', views.consultar_detalle_mantenimiento,name='consultar_detalle_matenimiento'),
    path('crear_detalle_mantenimiento/', views.crear_detalle_mantenimiento,name='crear_detalle_mantenimiento'),
    path('eliminar_detalle_mantenimiento/<int:id>', views.eliminar_detalle_mantenimiento,name='eliminar_detalle_mantenimiento'),
    path('modificar_detalle_mantenimiento/<int:id>', views.modificar_detalle_mantenimiento,name='modificar_detalle_mantenimiento'),



##-------ruta para entidad devolucion-----##
    path('consultar_devolucion/', views.consultar_devolucion,name='consultar_devolucion'),
    path('crear_devolucion/', views.crear_devolucion,name='crear_devolucion'),
    path('eliminar_devolucion/<int:id>', views.eliminar_devolucion,name='eliminar_devolucion'),
    path('modificar_devolucion/<int:id>', views.modificar_devolucion,name='modificar_devolucion'),



##-------ruta para entidad empleado-----##
    path('consultar_empleado/', views.consultar_empleado,name='consultar_empleado'),
    path('crear_empleado/', views.crear_empleado,name='crear_empleado'),
    path('eliminar_empleado/<int:id>', views.eliminar_empleado,name='eliminar_empleado'),
    path('modificar_empleado/<int:id>', views.modificar_empleado,name='modificar_empleado'),


##-------ruta para entidad equipo-----##
    path('consultar_equipo/', views.consultar_equipo,name='consultar_equipo'),
    path('crear_equipo/', views.crear_equipo,name='crear_equipo'),
    path('eliminar_equipo/<int:id>', views.eliminar_equipo,name='eliminar_equipo'),
    path('modificar_equipo/<int:id>', views.modificar_equipo,name='modificar_equipo'),




##-------ruta para entidad factura -----##
    path('consultar_factura/', views.consultar_factura,name='consultar_factura'),
    path('crear_factura/', views.crear_factura,name='crear_factura'),
    path('eliminar_factura/<int:id>', views.eliminar_factura,name='eliminar_factura'),
    path('modificar_factura/<int:id>', views.modificar_factura,name='modificar_factura'),



##-------ruta para entidad forma_de_pago-----##
    path('consultar_forma_de_pago/', views.consultar_forma_de_pago,name='consultar_forma_de_pago'),
    path('crear_forma_de_pago/', views.crear_forma_de_pago,name='crear_forma_de_pago'),
    path('eliminar_forma_de_pago/<int:id>', views.eliminar_forma_de_pago,name='eliminar_forma_de_pago'),
    path('modificar_forma_de_pago/<int:id>', views.modificar_forma_de_pago,name='modificar_forma_de_pago'),



##-------ruta para entidad mantenimiento-----##
    path('consultar_mantenimineto/', views.consultar_mantenimiento,name='consultar_mantenimiento'),
    path('crear_mantenimiento/', views.crear_mantenimiento,name='crear_mantenimiento'),
    path('eliminar_mantenimiento/<int:id>', views.eliminar_mantenimiento,name='eliminar_mantenimiento'),
    path('modificar_mantenimiento/<int:id>', views.modificar_mantenimiento,name='modificar_mantenimiento'),



##-------ruta para entidad producto-----##
    path('consultar_producto/', views.consultar_producto,name='consultar_producto'),
    path('crear_producto/', views.crear_producto,name='crear_producto'),
    path('eliminar_producto/<int:id>', views.eliminar_producto,name='eliminar_producto'),
    path('modificar_producto/<int:id>', views.modificar_producto,name='modificar_producto'),



##-------ruta para entidad proveedor-----##
    path('consultar_proveedor/', views.consultar_proveedor,name='consultar_proveedor'),
    path('crear_proveedor/', views.crear_proveedor,name='crear_proveedor'),
    path('eliminar_proveedor/<int:id>', views.eliminar_proveedor,name='eliminar_proveedor'),
    path('modificar_proveedor/<int:id>', views.modificar_proveedor,name='modificar_proveedor'),



##-------ruta para entidad servicio-----##
    path('consultar_servicio/', views.consultar_servicio,name='consultar_servicio'),
    path('crear_servicio/', views.crear_servicio,name='crear_servicio'),
    path('eliminar_servicio/<int:id>', views.eliminar_servicio,name='eliminar_servicio'),
    path('modificar_servicio/<int:id>', views.modificar_servicio,name='modificar_servicio'),



##-------ruta para entidad tipo_de_documento-----##
    path('consultar_tipo_de_documento/', views.consultar_tipo_de_documento,name='consultar_tipo_de_documento'),
    path('crear_tipo_de_documento/', views.crear_tipo_de_documento,name='crear_tipo_de_documento'),
    path('eliminar_tipo_de_documento/<int:id>', views.eliminar_tipo_de_documento,name='eliminar_tipo_de_documento'),
    path('modificar_tipo_de_documento/<int:id>', views.modificar_tipo_de_documento,name='modificar_tipo_de_documento'),














]
