from django.forms import ModelForm
from django import forms
from .models import cliente, proveedor, ciudad, cargo, detalle_mantenimiento, categoria, empleado, forma_de_pago, factura, producto, detalle_factura, devolucion, equipo, servicio, mantenimiento, tipo_de_documento

class Buscar_cedula(forms.Form):
    identificacion = forms.CharField(label="identificacion",required=True)

class Buscar_por_fecha(forms.Form):
    desde = forms.DateTimeField(label="Desde", required=True, widget=forms.DateInput(format=('%Y-%m-%d'),
                                                                                     attrs={
                                                                                         'placeholder': 'Select a date',
                                                                                         'type': 'date', 'size': 40}))

    hasta = forms.DateTimeField(label="Hasta", required=True, widget=forms.DateInput(format=('%Y-%m-%d'),
                                                                                     attrs={
                                                                                         'placeholder': 'Select a date',
                                                                                         'type': 'date', 'size': 40}))


class Buscarpornombre_cliente(forms.Form):
    nombre_cliente = forms.CharField(label="nombre_cliente", required=True)


class ClienteForm(forms.ModelForm):
    class Meta:
        model = cliente
        fields = ['Tipo_Documento','identificacion','nombre_cliente','ciudad1','direccion','celular','correo',]


class Buscarpornombre_comercial(forms.Form):
    nombre_comercial = forms.CharField(label="nombre_comercial", required=True)


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = proveedor
        fields = ['nombre_proveedor','nombre_comercial','direccion','telefono','Ciudad1']




class Buscarpornombre_ciudad(forms.Form):
    nombre_ciudad = forms.CharField(label="nombre_ciudad", required=True)

class CiudadForm(forms.ModelForm):
    class Meta:
        model = ciudad
        fields = ['nombre_ciudad']



class Buscarpornombre_cargo(forms.Form):
    nombre_cargo = forms.CharField(label="nombre_cargo", required=True)

class CargoForm(forms.ModelForm):
    class Meta:
        model = cargo
        fields = ['nombre_cargo']



class Buscarpordescripcion_mantenimiento(forms.Form):
    descripcion = forms.CharField(label="descripcion_mantenimiento", required=True)

class Detalle_MantenimientoForm(forms.ModelForm):
    class Meta:
        model = detalle_mantenimiento
        fields= ['descripcion_mantenimiento']



class Buscarpordescripcion_categoria(forms.Form):
    descripcion_categoria = forms.CharField(label="descripcion_categoria", required=True)

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = categoria
        fields =['descripcion_categoria']


class Buscarpornombre_empleado(forms.Form):
    n_empleado = forms.CharField(label="nombre_empleado", required=True)

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = empleado
        fields = ['nombre_empleado','cedula',]


class Buscarpordescripcion_forma_de_pago(forms.Form):
    descripcion_forma_de_pago = forms.CharField(label="descripcion_forma_de_pago", required=True)

class Forma_de_pagoForm(forms.ModelForm):
    class  Meta:
        model = forma_de_pago
        fields = ['descripcion_forma_de_pago']


class Buscarporfecha_facturacion(forms.Form):
    fecha_facturacion = forms.CharField(label="fecha_facturacion", required=True)

class FacturaForm(forms.ModelForm):
    class Meta:
        model = factura
        fields = ['fecha_facturacion','total_factura','iva']



class Buscarpordescripcion(forms.Form):
    descripcion = forms.CharField(label="descripcion", required=True)

class ProductoForm(forms.ModelForm):
    class Meta:
        model = producto
        fields = ['descripcion','precio_venta','precio_costo','stock','fecha_ingreso']



class Buscarporcantidad(forms.Form):
    cantidad = forms.CharField(label="cantidad", required=True)

class Detalle_facturaForm(forms.ModelForm):
    class Meta:
        model = detalle_factura
        fields = ['cantidad','total']


class Buscarporfecha_devolucion(forms.Form):
    fecha_devolucion = forms.CharField(label="fecha_devolucion", required=True)

class DevolucionForm(forms.ModelForm):
    class Meta:
        model = devolucion
        fields = ['motivo','fecha_devolucion','cantidad']

class Buscarpornombre_equipo(forms.Form):
    nombre_equipo = forms.CharField(label="nombre_equipo", required=True)


class EquipoForm(forms.ModelForm):
    class Meta:
        model = equipo
        fields = ['nombre_equipo','marca','serie']



class Buscarpornombre_servicios(forms.Form):
    nombre_servicios = forms.CharField(label="nombre_servicios", required=True)

class ServicioForm(forms.ModelForm):
    class Meta:
        model = servicio
        fields = ['nombre_de_servicios','precios']



class Buscarporfecha_retiro(forms.Form):
    fecha_retiro = forms.CharField(label="fecha_retiro", required=True)

class MantenimientoForm(forms.ModelForm):
    class Meta:
        model = mantenimiento
        fields = ['fecha_retiro','observacion_retiro','fecha_entrega','observacion_entrega']

class Buscarportipo_de_documento(forms.Form):
    documento = forms.CharField(label="tipo_de_documento", required=True)

class Tipo_de_documentoForm(forms.ModelForm):
    class Meta:
        model = tipo_de_documento
        fields = ['documento']








