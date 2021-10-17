from django.db import models


# Create your models here.
class cargo(models.Model):
    nombre_cargo = models.CharField(max_length=25)

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = 'tp_cargo'
        verbose_name = "cargo"
        verbose_name_plural = "cargos"

    def __str__(self):
        return "{}".format(self.nombre_cargo)


class detalle_mantenimiento(models.Model):
    descripcion_mantenimiento = models.CharField(max_length=200)

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = 'tp_detalle_mantenimineto'
        verbose_name = "Detalle_mantenimiento"
        verbose_name_plural = "Detalle_mantenimientos"

    def __str__(self):
        return "{}".format(self.descripcion_mantenimiento)


class categoria(models.Model):
    descripcion_categoria = models.CharField(max_length=25)

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = 'tp_categoria'
        verbose_name = "categoria"
        verbose_name_plural = "categorias"

    def __str__(self):
        return "{}".format(self.descripcion_categoria)


class ciudad(models.Model):
    nombre_ciudad = models.CharField(max_length=25)

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = 'tp_ciudad'
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"

    def __str__(self):
        return "{}".format(self.nombre_ciudad)


class tipo_de_documento(models.Model):
    documento = models.CharField(max_length=25)

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default= 1)

    class Meta:
        db_table = 'tp_tipo_de_documento'
        verbose_name = "Tipo_De_Documento"
        verbose_name_plural = "Tipo_De_Documentos"

    def __str__(self):
        return "{}".format(self.documento)


class cliente(models.Model):
    Tipo_Documento = models.ForeignKey(tipo_de_documento, on_delete=models.CASCADE)
    identificacion = models.CharField(max_length=13)
    nombre_cliente = models.CharField(max_length=50)
    ciudad1 = models.ForeignKey(ciudad, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=100)
    celular = models.CharField(max_length=15)
    correo = models.EmailField(null=True, blank=True)

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = 'tp_cliente'

    def __str__(self):
        return "{}{}{} ".format(self.nombre_cliente, "    ", self.direccion)


class proveedor(models.Model):
    nombre_proveedor = models.CharField(max_length=100)
    nombre_comercial = models.CharField(max_length=100)
    direccion = models.CharField(max_length=250)
    telefono = models.CharField(max_length=15)
    Ciudad1 = models.ForeignKey(ciudad, on_delete=models.CASCADE)

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = 'tp_proveedor'

    def __str__(self):
        return "{}{}{} ".format(self.nombre_proveedor, "    ", self.direccion)


class empleado(models.Model):
    nombre_empleado = models.CharField(max_length=100)
    cedula = models.CharField(max_length=15)

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = 'tp_empleado'
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"

    def __str__(self):
        return "{}".format(self.nombre_empleado, "  ", self.cedula)


class forma_de_pago(models.Model):
    descripcion_forma_de_pago = models.CharField(max_length=100)

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = 'tp_forma_de_pago'
        verbose_name = "Forma_de_pago"
        verbose_name_plural = "Forma_de_pagos"

    def __str__(self):
        return "{}".format(self.descripcion_forma_de_pago)


class producto(models.Model):
    descripcion = models.CharField(max_length=100)
    precio_venta = models.DecimalField(max_digits=7, decimal_places=2)
    precio_costo = models.DecimalField(max_digits=7, decimal_places=2)
    stock = models.IntegerField()
    fecha_ingreso = models.DateTimeField()

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = 'tp_producto'
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return "{}".format(self.descripcion, " ", self.fecha_ingreso)

class factura(models.Model):
    fecha_facturacion = models.DateTimeField()
    total_factura = models.DecimalField(max_digits=7, decimal_places=2)
    iva = models.DecimalField(max_digits=7, decimal_places=2)
    producto_v = models.ForeignKey(producto,on_delete=models.CASCADE, related_name='productos')

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = 'tp_factura'
        verbose_name = "Factura"
        verbose_name_plural = "Factura"

    def __str__(self):
        return "{}".format(self.fecha_facturacion, " ", self.total_factura)





class detalle_factura(models.Model):
    # cliente = models.ForeignKey(cliente,on_delete=models.CASCADE)
    # empleado =models.ForeignKey(empleado,on_delete=models.CASCADE)

    cantidad = models.CharField(max_length=100)
    total = models.DecimalField(max_digits=7, decimal_places=2)

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = 'tp_detalle_factura'
        verbose_name = "Detalle_factura"
        verbose_name_plural = "Detalle_factura"

    def __str__(self):
        return "{}".format(self.cantidad, " ", self.total)


class devolucion(models.Model):
    motivo = models.CharField(max_length=100)
    fecha_devolucion = models.DateTimeField()
    cantidad = models.CharField(max_length=100)

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = 'tp_devolucion'
        verbose_name = "Devolucion"
        verbose_name_plural = "Devolucion"

    def __str__(self):
        return "{}".format(self.motivo, " ", self.cantidad)


class equipo(models.Model):
    nombre_equipo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    serie = models.CharField(max_length=100)

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = 'tp_equipo'
        verbose_name = "Equipo"
        verbose_name_plural = "Equipo"

    def __str__(self):
        return "{}".format(self.nombre_equipo, " ", self.serie)


class servicio(models.Model):
    nombre_de_servicios = models.CharField(max_length=100)
    precios = models.DecimalField(max_digits=7, decimal_places=2)

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = 'tp_servicio'
        verbose_name = "Servicio"
        verbose_name_plural = "Servicio"

    def __str__(self):
        return "{}".format(self.nombre_de_servicios, " ", self.precios)


class mantenimiento(models.Model):
    fecha_retiro = models.DateTimeField()
    observacion_retiro = models.CharField(max_length=100)
    fecha_entrega = models.DateTimeField()
    observacion_entrega = models.CharField(max_length=100)

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = 'tp_mantenimiento'
        verbose_name = "Mantenimiento"
        verbose_name_plural = "Mantenimiento"

    def __str__(self):
        return "{}".format(self.fecha_retiro, " ", self.observacion_entrega)
