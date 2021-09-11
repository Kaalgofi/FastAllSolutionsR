from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import ClienteForm, ProveedorForm, CiudadForm
from .models import cliente, ciudad
# Create your views here.
def login(request):
    return render(request, "index.html")

def saludo(request):
    return HttpResponse("Hola Mundo")

def miprimerafuncion (request):
    return render(request, "base.html")



##-------------- categoria -------------##

def crear_categoria (request):
    return render(request, "categoria/crear_categoria.html")
def consultar_categoria (request):
    return render(request, "categoria/consultar_categoria.html")
def eliminar_categoria (request):
    return render(request, "categoria/eliminar_categoria.html")
def modificar_categoria (request):
    return render(request, "categoria/modificar_categoria.html")

##---------------- cliente ------------##

def crear_cliente (request):
    if request.method == "POST":
        clienteForm = ClienteForm(request.POST)
        if clienteForm.is_valid():
            clienteForm.save()
            return redirect('consultar_cliente')
        else:
            clienteForm = ClienteForm()
    else:
        clienteForm = ClienteForm()

    return render(request, "cliente/crear_cliente.html" , {'cliente': clienteForm})

def consultar_cliente (request):
    cliente_p = cliente.objects.all()
    return render(request, "cliente/consultar_cliente.html" , {'cliente_ls': cliente_p})

def eliminar_cliente (request,id):
    if request.method == "POST":
        clienten = get_object_or_404(cliente, pk=id)
        clienteForm = ClienteForm(request.POST or None, instance=clienten)
        if clienteForm.is_valid():
            clienten.estado = 0
            clienten.save()
            return redirect('consultar_cliente')

    else:
        clienten = get_object_or_404(cliente, pk=id)
        clienteForm = ClienteForm(request.POST or None, instance=clienten)
    return render(request, "cliente/eliminar_cliente.html", {'clienteform': clienteForm})


def modificar_cliente (request,id):
    if request.method == "POST":
        clienten = get_object_or_404(cliente, pk=id)
        clienteForm = ClienteForm(request.POST or None, instance=clienten)
        if clienteForm.is_valid():
            clienteForm.save()
            return redirect('consultar_cliente')
        else:
            clienteForm = ClienteForm(instance=clienten)
    else:  ##GET
        clienten = get_object_or_404(cliente, pk=id)
        clienteForm = ClienteForm(request.POST or None, instance=clienten)

        return render(request, "cliente/modificar_cliente.html", {'clienteform': clienteForm})


##-------------- devolucion -------------##

def crear_devoluciones (request):
    return render(request, "devolucion/crear_devolucion.html")
def consultar_devoluciones (request):
    return render(request, "devolucion/consultar_devolucion.html")
def eliminar_devoluciones (request):
    return render(request, "devolucion/eliminar_devolucion.html")
def modificar_devoluciones (request):
    return render(request, "devolucion/modificar_devolucion.html")


##-------------- factura -------------##

def crear_factura (request):
    return render(request, "factura/crear_factura.html")
def consultar_factura (request):
    return render(request, "factura/consultar_factura.html")
def eliminar_factura (request):
    return render(request, "factura/eliminar_factura.html")
def modificar_factura (request):
    return render(request, "factura/modificar_factura.html")

##-------------- forma_de_pago -------------##

def crear_forma_de_pago (request):
    return render(request, "forma_de_pago/crear_forma_de_pago.html")
def consultar_forma_de_pago (request):
    return render(request, "forma_de_pago/consultar_forma_de_pago.html")
def eliminar_forma_de_pago (request):
    return render(request, "forma_de_pago/eliminar_forma_de_pago.html")
def modificar_forma_de_pago (request):
    return render(request, "forma_de_pago/modificar_forma_de_pago.html")


##-------------- producto/ -------------##

def crear_producto (request):
    return render(request, "producto/crear_producto.html")
def consultar_producto (request):
    return render(request, "producto/consultar_producto.html")
def eliminar_producto (request):
    return render(request, "producto/eliminar_producto.html")
def modificar_producto (request):
    return render(request, "producto/modificar_producto.html")

##-------------- proveedor -------------##

def crear_proveedor (request):
    if request.method == "POST":
        proveedorForm = ProveedorForm(request.POST)
        if proveedorForm.is_valid():
            proveedorForm.save()
            return redirect('consultar_proveedor')
        else:
            proveedorForm = ProveedorForm()
    else:
        proveedorForm = ProveedorForm()
    return render(request, "proveedor/crear_proveedor.html",{'proveedor': proveedorForm})
def consultar_proveedor (request):
    return render(request, "proveedor/consultar_proveedor.html")
def eliminar_proveedor (request):
    return render(request, "proveedor/eliminar_proveedor.html")
def modificar_proveedor (request):
    return render(request, "proveedor/modificar_proveedor.html")



##-------------- empleado -------------##

def crear_empleado (request):
    if request.method == "POST":
        clienteForm = ClienteForm(request.POST)
        if clienteForm.is_valid():
            clienteForm.save()
            return redirect('consultar_cliente')
        else:
            clienteForm = ClienteForm()
    else:
        clienteForm = ClienteForm()
    return render(request, "empleado/crear_empleado.html")
def consultar_empleado (request):
    return render(request, "empleado/consultar_empleado.html")
def eliminar_empleado (request):
    return render(request, "empleado/eliminar_empleado.html")
def modificar_empleado (request):
    return render(request, "empleado/modificar_empleado.html")



##-------------- tipo_de_documento -------------##

def crear_tipo_de_documento (request):
    return render(request, "tipo_de_documento/crear_tipo_de_documento.html")
def consultar_tipo_de_documento (request):
    return render(request, "tipo_de_documento/consultar_tipo_de_documento.html")
def eliminar_tipo_de_documento (request):
    return render(request, "tipo_de_documento/eliminar_tipo_de_documento.html")
def modificar_tipo_de_documento (request):
    return render(request, "tipo_de_documento/modificar_tipo_de_documento.html")


##-------------- tipo_de_documento -------------##

def crear_detalle_factura (request):
    return render(request, "detalle_factura/crear_detalle_factura.html")
def consultar_detalle_factura (request):
    return render(request, "detalle_factura/consultar_detalle_factura.html")
def eliminar_detalle_factura (request):
    return render(request, "detalle_factura/eliminar_detalle_factura.html")
def modificar_detalle_factura (request):
    return render(request, "detalle_factura/modificar_detalle_factura.html")


##-------------- ciudad -------------##

def crear_ciudad (request):
    if request.method == "POST":
        ciudadForm = CiudadForm(request.POST)
        if ciudadForm.is_valid():
            ciudadForm.save()
            return redirect('consultar_ciudad')
        else:
            ciudadForm = CiudadForm()
    else:
        ciudadForm = CiudadForm()

    return render(request, "ciudad/crear_ciudad.html" , {'ciudad': ciudadForm})

def consultar_ciudad (request):
    ciudad_p = ciudad.objects.all()

    return render(request, "ciudad/consultar_ciudad.html", {'ciudad1': ciudad_p})
def eliminar_ciudad (request,id):
    if request.method == "POST":
        ciudad1 = get_object_or_404(ciudad, pk=id)
        ciudadForm = CiudadForm(request.POST or None, instance=ciudad1)
        if ciudadForm.is_valid():
            ciudad1.estado = 0
            ciudad1.save()
            return redirect('consultar_ciudad')

    else:
        ciudad1 = get_object_or_404(ciudad, pk=id)
        ciudadForm = CiudadForm(request.POST or None, instance=ciudad1)

    return render(request, "ciudad/eliminar_ciudad.html",{'ciudad1': ciudadForm})

def modificar_ciudad (request,id):

    if request.method == "POST":
        ciudad1 = get_object_or_404(ciudad, pk=id)
        ciudadForm = CiudadForm(request.POST or None, instance=ciudad1)
        if ciudadForm.is_valid():
            ciudadForm.save()
            return redirect('consultar_ciudad')
        else:
            ciudadForm = CiudadForm(instance=ciudad1)
    else:  ##GET
        ciudad1 = get_object_or_404(ciudad, pk=id)
        ciudadForm = CiudadForm(request.POST or None, instance=ciudad1)
    return render(request, "ciudad/modificar_ciudad.html",{'ciudad1': ciudadForm})
