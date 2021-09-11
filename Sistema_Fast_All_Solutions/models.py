from django.db import models


# Create your models here.
class ciudad (models.Model):
    nombre_ciudad = models.CharField(max_length=50)

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = 'tp_ciudad'
        verbose_name="Ciudad"
        verbose_name_plural="Ciudades"

    def __str__(self):
     return "{}".format(self.nombre_ciudad)


class cliente (models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=100)
    edad = models.CharField(max_length=3)
    direccion = models.CharField(max_length=250)
    cedula = models.CharField(max_length=10)
    correo = models.EmailField(null=True, blank=True)
    ciudad1 = models.ForeignKey(ciudad, on_delete=models.CASCADE)

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = 'tp_cliente'

    def __str__(self):
        return "{}{}{} ".format(self.nombre, "    ", self.apellido)


class proveedor(models.Model):
    ruc = models.CharField(max_length=13)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=250)
    telefono = models.CharField(max_length=10)
    correo = models.EmailField(null=True, blank=True)
    Ciudad1 = models.ForeignKey(ciudad, on_delete=models.CASCADE)


    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = 'tp_proveedor'

    def __str__(self):
        return "{}{}{} ".format(self.nombre, "    ", self.direccion)
