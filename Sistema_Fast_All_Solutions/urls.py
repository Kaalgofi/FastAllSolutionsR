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



##-------ruta para entidad categoria-----##
    path('consultar_categoria/', views.consultar_categoria,name='consultar_categoria'),
    path('crear_categoria/', views.crear_categoria,name='crear_categoria'),
    path('eliminar_categoria/', views.eliminar_categoria,name='eliminar_categoria'),
    path('modificar_categoria/', views.modificar_categoria,name='modificar_categoria'),



##-------ruta para entidad cliente-----##
    path('consultar_cliente/', views.consultar_cliente,name='consultar_cliente'),
    path('crear_cliente/', views.crear_cliente,name='crear_cliente'),
    path('eliminar_cliente/<int:id>', views.eliminar_cliente,name='eliminar_cliente'),
    path('modificar_cliente/<int:id>', views.modificar_cliente,name='modificar_cliente'),



##-------ruta para entidad devolucion-----##
    path('consultar_devolucion/', views.consultar_devoluciones,name='consultar_devolucion'),
    path('crear_devolucion/', views.crear_devoluciones,name='crear_devolucion'),
    path('eliminar_devolucion/', views.eliminar_devoluciones,name='eliminar_devolucion'),
    path('modificar_devolucion/', views.modificar_devoluciones,name='modificar_devolucion'),



##-------ruta para entidad factura -----##
    path('consultar_factura/', views.consultar_factura,name='consultar_factura'),
    path('crear_factura/', views.crear_factura,name='crear_factura'),
    path('eliminar_factura/', views.eliminar_factura,name='eliminar_factura'),
    path('modificar_factura/', views.modificar_factura,name='modificar_factura'),



##-------ruta para entidad forma_de_pago-----##
    path('consultar_forma_de_pago/', views.consultar_forma_de_pago,name='consultar_forma_de_pago'),
    path('crear_forma_de_pago/', views.crear_forma_de_pago,name='crear_forma_de_pago'),
    path('eliminar_forma_de_pago/', views.eliminar_forma_de_pago,name='eliminar_forma_de_pago'),
    path('modificar_forma_de_pago/', views.modificar_forma_de_pago,name='modificar_forma_de_pago'),


##-------ruta para entidad producto-----##
    path('consultar_producto/', views.consultar_producto,name='consultar_producto'),
    path('crear_producto/', views.crear_producto,name='crear_producto'),
    path('eliminar_producto/', views.eliminar_producto,name='eliminar_producto'),
    path('modificar_producto/', views.modificar_producto,name='modificar_producto'),

##-------ruta para entidad proveedor-----##
    path('consultar_proveedor/', views.consultar_proveedor,name='consultar_proveedor'),
    path('crear_proveedor/', views.crear_proveedor,name='crear_proveedor'),
    path('eliminar_proveedor/', views.eliminar_proveedor,name='eliminar_proveedor'),
    path('modificar_proveedor/', views.modificar_proveedor,name='modificar_proveedor'),




##-------ruta para entidad empleado-----##
    path('consultar_empleado/', views.consultar_empleado,name='consultar_empleado'),
    path('crear_empleado/', views.crear_empleado,name='crear_empleado'),
    path('eliminar_empleado/<int:id>', views.eliminar_empleado,name='eliminar_empleado'),
    path('modificar_empleado/<int:id>', views.modificar_empleado,name='modificar_empleado'),


##-------ruta para entidad tipo_de_documento-----##
    path('consultar_tipo_de_documento/', views.consultar_tipo_de_documento,name='consultar_tipo_de_documento'),
    path('crear_tipo_de_documento/', views.crear_tipo_de_documento,name='crear_tipo_de_documento'),
    path('eliminar_tipo_de_documento/', views.eliminar_tipo_de_documento,name='eliminar_tipo_de_documento'),
    path('modificar_tipo_de_documento/', views.modificar_tipo_de_documento,name='modificar_tipo_de_documento'),


##-------ruta para entidad detalle_factura-----##
    path('consultar_detalle_factura/', views.consultar_detalle_factura,name='consultar_detalle_factura'),
    path('crear_detalle_factura/', views.crear_detalle_factura,name='crear_detalle_factura'),
    path('eliminar_detalle_factura/', views.eliminar_detalle_factura,name='eliminar_detalle_factura'),
    path('modificar_detalle_factura/', views.modificar_detalle_factura,name='modificar_detalle_factura'),



##-------ruta para entidad ciudad-----##
    path('consultar_ciudad/', views.consultar_ciudad,name='consultar_ciudad'),
    path('crear_ciudad/', views.crear_ciudad,name='crear_ciudad'),
    path('eliminar_ciudad/<int:id>', views.eliminar_ciudad,name='eliminar_ciudad'),
    path('modificar_ciudad/<int:id>', views.modificar_ciudad,name='modificar_ciudad'),








]
