from django.forms import ModelForm
from .models import cliente, proveedor, ciudad
class ClienteForm(ModelForm):
    class Meta:
        model = cliente
        fields = ['nombre', 'apellido', 'edad', 'direccion', 'cedula', 'correo','ciudad1']


class ProveedorForm(ModelForm):
    class Meta:
        model = proveedor
        fields = ['ruc', 'nombre', 'direccion', 'telefono', 'correo','Ciudad1']



class CiudadForm(ModelForm):
    class Meta:
        model = ciudad
        fields = ['nombre_ciudad']