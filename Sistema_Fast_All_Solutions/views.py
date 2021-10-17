from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import ClienteForm, ProveedorForm, CiudadForm, CargoForm, Detalle_MantenimientoForm, DevolucionForm, \
    EmpleadoForm, EquipoForm, CategoriaForm, ProductoForm, ServicioForm, Forma_de_pagoForm, FacturaForm, \
    MantenimientoForm,Detalle_facturaForm, Tipo_de_documentoForm, Buscarporfecha_devolucion, Buscarporfecha_retiro, Buscarporfecha_facturacion,\
    Buscarporfecha_ingreso, Buscarpordescripcion_forma_de_pago,Buscarproducto_v, Buscarpordescripcion_mantenimiento, Buscarpordescripcion_categoria, \
    Buscarpornombre_cliente, Buscarpornombre_empleado, Buscarpornombre_equipo, Buscarpornombre_comercial, Buscarpornombre_servicios,\
    Buscarpornombre_cargo, Buscarpornombre_ciudad, Buscar_por_fecha, Buscarporcantidad, Buscarportipo_de_documento, Buscar_cedula
from .models import cliente, ciudad, cargo, categoria, detalle_factura, detalle_mantenimiento, devolucion, empleado, equipo, factura,\
    forma_de_pago, mantenimiento, producto, proveedor, servicio, tipo_de_documento
# Create your views here.
def login(request):
    return render(request, "index.html")

def saludo(request):
    return HttpResponse("Hola Mundo")
@login_required(None, "", 'login')
def miprimerafuncion (request):
    return render(request, "base.html")


##---------------- cargo ------------##
@login_required(None, "", 'login')
def crear_cargo (request):
    if request.method == "POST":
        cargoForm = CargoForm(request.POST)
        if cargoForm.is_valid():
            cargoForm.save()
            return redirect('consultar_cargo')
        else:
            cargoForm = CargoForm()
    else:
        cargoForm = CargoForm()

    return render(request, "cargo/crear_cargo.html" , {'cargo': cargoForm})

@login_required(None, "", 'login')
def consultar_cargo (request):
    buscarpornombre_cargo = Buscarpornombre_cargo()

    cargo_p = None

    if request.method == "POST":

        buscarpornombre_cargo = Buscarpornombre_cargo(request.POST or None)
        if buscarpornombre_cargo.is_valid():

            nombre_cargo = buscarpornombre_cargo.cleaned_data['nombre_cargo']

            cargo_p = cargo.objects.filter(nombre_cargo__startswith=nombre_cargo)
    else:

          cargo_p = cargo.objects.all()
    return render(request, "cargo/consultar_cargo.html" , {'cargo_ls': cargo_p,'buscarpornombre_cargo':buscarpornombre_cargo})

@login_required(None, "", 'login')
def eliminar_cargo (request,id):
    if request.method == "POST":
        cargon = get_object_or_404(cargo, pk=id)
        cargoForm = CargoForm(request.POST or None, instance=cargon)
        if cargoForm.is_valid():
            cargon.estado = 0
            cargon.save()
            return redirect('consultar_cargo')

    else:
        cargon = get_object_or_404(cargo, pk=id)
        cargoForm = CargoForm(request.POST or None, instance=cargon)
    return render(request, "cargo/eliminar_cargo.html", {'cargoform': cargoForm})


@login_required(None, "", 'login')
def modificar_cargo (request,id):
    if request.method == "POST":
        cargon = get_object_or_404(cargo, pk=id)
        cargoForm = CargoForm(request.POST or None, instance=cargon)
        if cargoForm.is_valid():
            cargoForm.save()
            return redirect('consultar_cargo')
        else:
            cargoForm = CargoForm(instance=cargon)
    else:  ##GET
        cargon = get_object_or_404(cargo, pk=id)
        cargoForm = CargoForm(request.POST or None, instance=cargon)

    return render(request, "cargo/modificar_cargo.html", {'cargoform': cargoForm})

#-------------------------------------------------------------------------------------------------------#

##---------------- categoria ------------##

@login_required(None, "", 'login')
def crear_categoria (request):
    if request.method == "POST":
        categoriaForm = CategoriaForm(request.POST)
        if categoriaForm.is_valid():
            categoriaForm.save()
            return redirect('consultar_categoria')
        else:
            categoriaForm = CategoriaForm()
    else:
        categoriaForm = CategoriaForm()

    return render(request, "categoria/crear_categoria.html" , {'categoria': categoriaForm})

@login_required(None, "", 'login')
def consultar_categoria (request):
    buscarpordescripcion_categoria = Buscarpordescripcion_categoria()

    categoria_p = None

    if request.method == "POST":

        buscarpordescripcion_categoria = Buscarpordescripcion_categoria(request.POST or None)
        if buscarpordescripcion_categoria.is_valid():
            #desde = buscarporfecha.cleaned_data['desde']
            #hasta = buscarporfecha.cleaned_data['hasta']
            descripcion_categoria = buscarpordescripcion_categoria.cleaned_data['descripcion_categoria']

            descripcion_categoria_p = categoria.objects.filter(descripcion_categoria__startswith=descripcion_categoria)
    else:

          categoria_p = categoria.objects.all()
    return render(request, "categoria/consultar_categoria.html" , {'categoria_ls': categoria_p,'buscarpordescripcion_categoria':buscarpordescripcion_categoria})


@login_required(None, "", 'login')
def eliminar_categoria (request,id):
    if request.method == "POST":
        categorian = get_object_or_404(categoria, pk=id)
        categoriaForm = CategoriaForm(request.POST or None, instance=categorian)
        if categoriaForm.is_valid():
            categorian.estado = 0
            categorian.save()
            return redirect('consultar_categoria')

    else:
        categorian = get_object_or_404(categoria, pk=id)
        categoriaForm = CategoriaForm(request.POST or None, instance=categorian)
    return render(request, "categoria/eliminar_categoria.html", {'categoriaform': categoriaForm})


@login_required(None, "", 'login')
def modificar_categoria (request,id):
    if request.method == "POST":
        categorian = get_object_or_404(categoria, pk=id)
        categoriaForm = CategoriaForm(request.POST or None, instance=categorian)
        if categoriaForm.is_valid():
            categoriaForm.save()
            return redirect('consultar_categoria')
        else:
            categoriaForm = CategoriaForm(instance=categorian)
    else:  ##GET
        categorian = get_object_or_404(categoria, pk=id)
        categoriaForm = CategoriaForm(request.POST or None, instance=categorian)

    return render(request, "categoria/modificar_categoria.html", {'categoriaform': categoriaForm})

#------------------------------------------------------------------------------------------------#
##---------------- ciudad ------------##


@login_required(None, "", 'login')
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


@login_required(None, "", 'login')
def consultar_ciudad (request):
    buscarpornombre_ciudad = Buscarporfecha_devolucion()

    ciudad_p = None

    if request.method == "POST":
        #buscarporfecha = Buscarporfecha(request.POST or None)
        buscarpornombre_ciudad = Buscarporfecha_devolucion(request.POST or None)
        if buscarpornombre_ciudad.is_valid():
            desde = buscarpornombre_ciudad.cleaned_data['desde']
            hasta = buscarpornombre_ciudad.cleaned_data['hasta']
            #nombre_ciudad = buscarpornombre_ciudad.cleaned_data['ciudad']

            ciudad_p = ciudad.objects.filter(fecha_creacion__range=(desde,hasta))
    else:

          ciudad_p = ciudad.objects.all()
    return render(request, "ciudad/consultar_ciudad.html" , {'ciudad_ls': ciudad_p,'buscarpornombre_ciudad':buscarpornombre_ciudad})

@login_required(None, "", 'login')
def eliminar_ciudad (request,id):
    if request.method == "POST":
        ciudadn = get_object_or_404(ciudad, pk=id)
        ciudadForm = CiudadForm(request.POST or None, instance=ciudadn)
        if ciudadForm.is_valid():
            ciudadn.estado = 0
            ciudadn.save()
            return redirect('consultar_ciudad')

    else:
        ciudadn = get_object_or_404(ciudad, pk=id)
        ciudadForm = CiudadForm(request.POST or None, instance=ciudadn)
    return render(request, "ciudad/eliminar_ciudad.html", {'ciudadform': ciudadForm})

@login_required(None, "", 'login')
def modificar_ciudad (request,id):
    if request.method == "POST":
        ciudadn = get_object_or_404(ciudad, pk=id)
        ciudadForm = CiudadForm(request.POST or None, instance=ciudadn)
        if ciudadForm.is_valid():
            ciudadForm.save()
            return redirect('consultar_ciudad')
        else:
            ciudadForm = CiudadForm(instance=ciudadn)
    else:  ##GET
        ciudadn = get_object_or_404(ciudad, pk=id)
        ciudadForm = CiudadForm(request.POST or None, instance=ciudadn)

    return render(request, "ciudad/modificar_ciudad.html", {'ciudadform': ciudadForm})

#---------------------------------------------------------------------------------------------------#
##---------------- cliente ------------##

@login_required(None, "", 'login')
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


@login_required(None, "", 'login')
def consultar_cliente (request):
    buscarcform = Buscar_cedula()
    cliente_p = None

    if request.method == "POST":
        buscarcform = Buscar_cedula(request.POST or None)
        if buscarcform.is_valid():
            identificacion = buscarcform.cleaned_data['identificacion']
            cliente_p = cliente.objects.filter(identificacion__icontains=identificacion)
    else:
        cliente_p = cliente.objects.all()

    return render(request, "cliente/consultar_cliente.html" , {'cliente_ls': cliente_p,'buscarpornombre_cliente':buscarcform})


@login_required(None, "", 'login')
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


@login_required(None, "", 'login')
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

#--------------------------------------------------------------------------------------------------#
##----------------detalle_factura------------##

@login_required(None, "", 'login')
def crear_detalle_factura (request):
    if request.method == "POST":
        detalle_facturaForm = Detalle_facturaForm(request.POST)
        if detalle_facturaForm.is_valid():
            detalle_facturaForm.save()
            return redirect('consultar_detalle_factura')
        else:
            detalle_facturaForm = Detalle_facturaForm()
    else:
        detalle_facturaForm = Detalle_facturaForm()

    return render(request, "detalle_factura/crear_detalle_factura.html" , {'detalle_factura': detalle_facturaForm})

@login_required(None, "", 'login')
def consultar_detalle_factura (request):
    buscarporcantidad = Buscarporcantidad()
    #buscarporfecha = Buscarporfecha()
    detalle_factura_p = None

    if request.method == "POST":
        #buscarporfecha = Buscarporfecha(request.POST or None)
        buscarporcantidad = Buscarporcantidad(request.POST or None)
        if buscarporcantidad.is_valid():
            #desde = buscarporfecha.cleaned_data['desde']
            #hasta = buscarporfecha.cleaned_data['hasta']
            cantidad = buscarporcantidad.cleaned_data['cantidad']

            detalle_factura_p = detalle_factura.objects.filter(cantidad__startswith=cantidad)
    else:

          detalle_factura_p = detalle_factura.objects.all()
    return render(request, "detalle_factura/consultar_detalle_factura.html" , {'detalle_factura_ls': detalle_factura_p,'buscarporcantidad':buscarporcantidad})

@login_required(None, "", 'login')
def eliminar_detalle_factura (request,id):
    if request.method == "POST":
        detalle_facturan = get_object_or_404(detalle_factura, pk=id)
        detalle_facturaForm = Detalle_facturaForm(request.POST or None, instance=detalle_facturan)
        if detalle_facturaForm.is_valid():
            detalle_facturan.estado = 0
            detalle_facturan.save()
            return redirect('consultar_detalle_factura')

    else:
        detalle_facturan = get_object_or_404(detalle_factura, pk=id)
        detalle_facturaForm = Detalle_facturaForm(request.POST or None, instance=detalle_facturan)
    return render(request, "detalle_factura/eliminar_detalle_factura.html", {'detalle_facturaform': detalle_facturaForm})


@login_required(None, "", 'login')
def modificar_detalle_factura (request,id):
    if request.method == "POST":
        detalle_facturan = get_object_or_404(detalle_factura, pk=id)
        detalle_facturaForm = Detalle_facturaForm(request.POST or None, instance=detalle_facturan)
        if detalle_facturaForm.is_valid():
            detalle_facturaForm.save()
            return redirect('consultar_detalle_factura')
        else:
            detalle_facturaForm = Detalle_facturaForm(instance=detalle_facturan)
    else:  ##GET
        detalle_facturan = get_object_or_404(detalle_factura, pk=id)
        detalle_facturaForm = Detalle_facturaForm(request.POST or None, instance=detalle_facturan)

    return render(request, "detalle_factura/modificar_detalle_factura.html", {'detalle_facturaform_m': detalle_facturaForm})

#----------------------------------------------------------------------------------------#
##----------------detalle_mantenimiento------------##

@login_required(None, "", 'login')
def crear_detalle_mantenimiento (request):
    if request.method == "POST":
        detalle_mantenimientoForm = Detalle_MantenimientoForm(request.POST)
        if detalle_mantenimientoForm.is_valid():
            detalle_mantenimientoForm.save()
            return redirect('consultar_detalle_mantenimiento')
        else:
            detalle_mantenimientoForm = Detalle_MantenimientoForm()
    else:
        detalle_mantenimientoForm = Detalle_MantenimientoForm()

    return render(request, "detalle_mantenimiento/crear_detalle_mantenimiento.html" , {'detalle_mantenimiento': detalle_mantenimientoForm})

@login_required(None, "", 'login')
def consultar_detalle_mantenimiento (request):
    buscarpordescripcion_mantenimiento = Buscarpordescripcion_mantenimiento()
    #buscarporfecha = Buscarporfecha()
    detalle_mantenimiento_p = None

    if request.method == "POST":
        #buscarporfecha = Buscarporfecha(request.POST or None)
        buscarpordescripcion_mantenimiento = Buscarpordescripcion_mantenimiento(request.POST or None)
        if buscarpordescripcion_mantenimiento.is_valid():
            #desde = buscarporfecha.cleaned_data['desde']
            #hasta = buscarporfecha.cleaned_data['hasta']
            descripcion = buscarpordescripcion_mantenimiento.cleaned_data['descripcion']

            detalle_mantenimiento_p = detalle_mantenimiento.objects.filter(descripcion_mantenimiento__icontains=descripcion)
    else:

          detalle_mantenimiento_p = detalle_mantenimiento.objects.all()
    return render(request, "detalle_mantenimiento/consultar_detalle_mantenimiento.html" , {'detalle_mantenimiento': detalle_mantenimiento_p,'buscarpordescripcion_mantenimiento':buscarpordescripcion_mantenimiento})


@login_required(None, "", 'login')
def eliminar_detalle_mantenimiento (request,id):
    if request.method == "POST":
        detalle_mantenimienton = get_object_or_404(detalle_mantenimiento, pk=id)
        detalle_mantenimientoForm = Detalle_MantenimientoForm(request.POST or None, instance=detalle_mantenimienton)
        if detalle_mantenimientoForm.is_valid():
            detalle_mantenimienton.estado = 0
            detalle_mantenimienton.save()
            return redirect('consultar_detalle_mantenimiento')

    else:
        detalle_mantenimienton = get_object_or_404(detalle_mantenimiento, pk=id)
        detalle_mantenimientoForm = Detalle_MantenimientoForm(request.POST or None, instance=detalle_mantenimienton)
    return render(request, "detalle_mantenimiento/eliminar_detalle_mantenimiento.html", {'detalle_mantenimientoform': detalle_mantenimientoForm})


@login_required(None, "", 'login')
def modificar_detalle_mantenimiento (request,id):
    if request.method == "POST":
        detalle_mantenimienton = get_object_or_404(detalle_mantenimiento, pk=id)
        detalle_mantenimientoForm = Detalle_MantenimientoForm(request.POST or None, instance=detalle_mantenimienton)
        if detalle_mantenimientoForm.is_valid():
            detalle_mantenimientoForm.save()
            return redirect('consultar_detalle_mantenimiento')
        else:
            detalle_mantenimientoForm = Detalle_MantenimientoForm(instance=detalle_mantenimienton)
    else:  ##GET
        detalle_mantenimienton = get_object_or_404(detalle_mantenimiento, pk=id)
        detalle_mantenimientoForm = Detalle_MantenimientoForm(request.POST or None, instance=detalle_mantenimienton)

    return render(request, "detalle_mantenimiento/modificar_detalle_mantenimiento.html", {'detalle_mantenimientoform': detalle_mantenimientoForm})
#----------------------------------------------------------------------------------------------------------------------------------#


##---------------- empleado ------------##

@login_required(None, "", 'login')
def crear_empleado (request):
    if request.method == "POST":
        empleadoForm = EmpleadoForm(request.POST)
        if empleadoForm.is_valid():
            empleadoForm.save()
            return redirect('consultar_empleado')
        else:
            empleadoForm = EmpleadoForm()
    else:
        empleadoForm = EmpleadoForm()

    return render(request, "empleado/crear_empleado.html" , {'empleado': empleadoForm})

@login_required(None, "", 'login')
def consultar_empleado (request):
    buscarpornombre_empleado = Buscarpornombre_empleado()
    empleado_p = None
    if request.method == "POST":
        buscarpornombre_empleado = Buscarpornombre_empleado(request.POST or None)
        if buscarpornombre_empleado.is_valid():
            n_empleado = buscarpornombre_empleado.cleaned_data['n_empleado']
            empleado_p = empleado.objects.filter(nombre_empleado__icontains=n_empleado)

    else:
        empleado_p = empleado.objects.all()

    return render(request, "empleado/consultar_empleado.html" , {'empleado_ls': empleado_p,'buscarpornombre_empleado':buscarpornombre_empleado})


@login_required(None, "", 'login')
def eliminar_empleado (request,id):
    if request.method == "POST":
        empleadon = get_object_or_404(empleado, pk=id)
        empleadoForm = EmpleadoForm(request.POST or None, instance=empleadon)
        if empleadoForm.is_valid():
            empleadon.estado = 0
            empleadon.save()
            return redirect('consultar_empleado')

    else:
        empleadon = get_object_or_404(empleado, pk=id)
        empleadoForm = EmpleadoForm(request.POST or None, instance=empleadon)
    return render(request, "empleado/eliminar_empleado.html", {'empleadoform': empleadoForm})


@login_required(None, "", 'login')
def modificar_empleado (request,id):
    if request.method == "POST":
        empleadon = get_object_or_404(empleado, pk=id)
        empleadoForm = EmpleadoForm(request.POST or None, instance=empleadon)
        if empleadoForm.is_valid():
            empleadoForm.save()
            return redirect('consultar_empleado')
        else:
            empleadoForm = EmpleadoForm(instance=empleadon)
    else:  ##GET
        empleadon = get_object_or_404(empleado, pk=id)
        empleadoForm = EmpleadoForm(request.POST or None, instance=empleadon)

        return render(request, "empleado/modificar_empleado.html", {'empleadoform': empleadoForm})
    #----------------------------------------------------------------------------------------------#


##---------------- equipo ------------##

@login_required(None, "", 'login')
def crear_equipo (request):
    if request.method == "POST":
        equipoForm = EquipoForm(request.POST)
        if equipoForm.is_valid():
            equipoForm.save()
            return redirect('consultar_equipo')
        else:
            equipoForm = EquipoForm()
    else:
        equipoForm = EquipoForm()

    return render(request, "equipo/crear_equipo.html" , {'equipo': equipoForm})


@login_required(None, "", 'login')
def consultar_equipo (request):
    buscarpornombre_equipo = Buscarpornombre_equipo()
    #buscarporfecha = Buscarporfecha()
    equipo_p = None

    if request.method == "POST":
        #buscarporfecha = Buscarporfecha(request.POST or None)
        buscarpornombre_equipo = Buscarpornombre_equipo(request.POST or None)
        if buscarpornombre_equipo.is_valid():
            #desde = buscarporfecha.cleaned_data['desde']
            #hasta = buscarporfecha.cleaned_data['hasta']
            nombre_equipo = buscarpornombre_equipo.cleaned_data['nombre_equipo']

            equipo_p = equipo.objects.filter(nombre_equipo__startswith=nombre_equipo)
    else:

          equipo_p = equipo.objects.all()
    return render(request, "equipo/consultar_equipo.html" , {'equipo_ls': equipo_p, 'buscarpornombre_equipo':buscarpornombre_equipo})


@login_required(None, "", 'login')
def eliminar_equipo (request,id):
    if request.method == "POST":
        equipon = get_object_or_404(equipo, pk=id)
        equipoForm = EquipoForm(request.POST or None, instance=equipon)
        if equipoForm.is_valid():
            equipon.estado = 0
            equipon.save()
            return redirect('consultar_equipo')

    else:
        equipon = get_object_or_404(equipo, pk=id)
        equipoForm = EquipoForm(request.POST or None, instance=equipon)
    return render(request, "equipo/eliminar_equipo.html", {'equipoform': equipoForm})


@login_required(None, "", 'login')
def modificar_equipo (request,id):
    if request.method == "POST":
        equipon = get_object_or_404(cliente, pk=id)
        equipoForm = EquipoForm(request.POST or None, instance=equipon)
        if equipoForm.is_valid():
            equipoForm.save()
            return redirect('consultar_equipo')
        else:
            equipoForm = EquipoForm(instance=equipon)
    else:  ##GET
        equipon = get_object_or_404(equipo, pk=id)
        equipoForm = EquipoForm(request.POST or None, instance=equipon)

    return render(request, "equipo/modificar_equipo.html", {'equipoform': equipoForm})
#----------------------------------------------------------------------------------------------#

##---------------- descripcion_forma_de_pago ------------##
@login_required(None, "", 'login')
def crear_forma_de_pago (request):
    if request.method == "POST":
        forma_de_pagoForm = Forma_de_pagoForm(request.POST)
        if forma_de_pagoForm.is_valid():
            forma_de_pagoForm.save()
            return redirect('consultar_forma_de_pago')
        else:
            forma_de_pagoForm = Forma_de_pagoForm()
    else:
        forma_de_pagoForm = Forma_de_pagoForm()

    return render(request, "forma_de_pago/crear_forma_de_pago.html" , {'forma_de_pago': forma_de_pagoForm})

@login_required(None, "", 'login')
def consultar_forma_de_pago (request):
    buscarpordescripcion_forma_de_pago = Buscarpordescripcion_forma_de_pago()
    #buscarporfecha = Buscarporfecha()
    forma_de_pago_p = None

    if request.method == "POST":
        #buscarporfecha = Buscarporfecha(request.POST or None)
        buscarpordescripcion_forma_de_pago = Buscarpordescripcion_forma_de_pago(request.POST or None)
        if buscarpordescripcion_forma_de_pago.is_valid():
            #desde = buscarporfecha.cleaned_data['desde']
            #hasta = buscarporfecha.cleaned_data['hasta']
            descripcion_forma_de_pago = buscarpordescripcion_forma_de_pago.cleaned_data['descripcion_forma_de_pago']

            forma_de_pago_p = forma_de_pago.objects.filter(descripcion_forma_de_pago__startswith=descripcion_forma_de_pago)
    else:

          forma_de_pago_p = forma_de_pago.objects.all()
    return render(request, "forma_de_pago/consultar_forma_de_pago.html" , {'forma_de_pago_ls': forma_de_pago_p,'buscarpordescripcion_forma_de_pago':buscarpordescripcion_forma_de_pago})


@login_required(None, "", 'login')
def eliminar_forma_de_pago (request,id):
    if request.method == "POST":
        forma_de_pagon = get_object_or_404(forma_de_pago, pk=id)
        forma_de_pagoForm = Forma_de_pagoForm(request.POST or None, instance=forma_de_pagon)
        if forma_de_pagoForm.is_valid():
            forma_de_pagon.estado = 0
            forma_de_pagon.save()
            return redirect('consultar_forma_de_pago')

    else:
        forma_de_pagon = get_object_or_404(forma_de_pago, pk=id)
        forma_de_pagoForm = Forma_de_pagoForm(request.POST or None, instance=forma_de_pagon)
    return render(request, "forma_de_pago/eliminar_forma_de_pago.html", {'forma_de_pagoform': forma_de_pagoForm})

@login_required(None, "", 'login')
def modificar_forma_de_pago (request,id):
    if request.method == "POST":
        forma_de_pagon = get_object_or_404(forma_de_pago, pk=id)
        forma_de_pagoForm = Forma_de_pagoForm(request.POST or None, instance=forma_de_pagon)
        if forma_de_pagoForm.is_valid():
            forma_de_pagoForm.save()
            return redirect('consultar_forma_de_pago')
        else:
            forma_de_pagoForm = Forma_de_pagoForm(instance=forma_de_pagon)
    else:  ##GET
        forma_de_pagon = get_object_or_404(forma_de_pago, pk=id)
        forma_de_pagoForm = Forma_de_pagoForm(request.POST or None, instance=forma_de_pagon)

    return render(request, "forma_de_pago/modificar_forma_de_pago.html", {'forma_de_pagoform': forma_de_pagoForm})
#----------------------------------------------------------------------------------------------#
##----------------mantenimiento ------------##

@login_required(None, "", 'login')
def crear_mantenimiento (request):
    if request.method == "POST":
        mantenimientoForm = MantenimientoForm(request.POST)
        if mantenimientoForm.is_valid():
            mantenimientoForm.save()
            return redirect('consultar_mantenimiento')
        else:
            mantenimientoForm = MantenimientoForm()
    else:
        mantenimientoForm = MantenimientoForm()

    return render(request, "mantenimiento/crear_mantenimiento.html" , {'mantenimiento': mantenimientoForm})


@login_required(None, "", 'login')
def consultar_mantenimiento (request):
    buscarporfecha_retiro = Buscarporfecha_retiro()
    #buscarporfecha = Buscarporfecha()
    mantenimiento_p = None

    if request.method == "POST":
        #buscarporfecha = Buscarporfecha(request.POST or None)
        buscarporfecha_retiro = Buscarporfecha_retiro(request.POST or None)
        if buscarporfecha_retiro.is_valid():
            #desde = buscarporfecha.cleaned_data['desde']
            #hasta = buscarporfecha.cleaned_data['hasta']
            fecha_retiro = buscarporfecha_retiro.cleaned_data['fecha_retiro']

            mantenimiento_p = mantenimiento.objects.filter(fecha_retiro__startswith=fecha_retiro)
    else:

          mantenimiento_p = mantenimiento.objects.all()
    return render(request, "mantenimiento/consultar_mantenimiento.html" , {'mantenimiento_ls': mantenimiento_p,'buscarporfecha_retiro':buscarporfecha_retiro})

@login_required(None, "", 'login')
def eliminar_mantenimiento (request,id):
    if request.method == "POST":
        mantenimienton = get_object_or_404(mantenimiento, pk=id)
        mantenimientoForm = MantenimientoForm(request.POST or None, instance=mantenimienton)
        if mantenimientoForm.is_valid():
            mantenimienton.estado = 0
            mantenimienton.save()
            return redirect('consultar_mantenimiento')

    else:
        mantenimienton = get_object_or_404(mantenimiento, pk=id)
        mantenimientoForm = MantenimientoForm(request.POST or None, instance=mantenimienton)
    return render(request, "mantenimiento/eliminar_mantenimiento.html", {'mantenimientoform': mantenimientoForm})

@login_required(None, "", 'login')
def modificar_mantenimiento (request,id):
    if request.method == "POST":
        mantenimienton = get_object_or_404(mantenimiento, pk=id)
        mantenimientoForm = MantenimientoForm(request.POST or None, instance=mantenimienton)
        if mantenimientoForm.is_valid():
            mantenimientoForm.save()
            return redirect('consultar_mantenimiento')
        else:
            mantenimientoForm = MantenimientoForm(instance=mantenimienton)
    else:  ##GET
        mantenimienton = get_object_or_404(mantenimiento, pk=id)
        mantenimientoForm = MantenimientoForm(request.POST or None, instance=mantenimienton)

    return render(request, "mantenimiento/modificar_mantenimiento.html", {'mantenimientoform': mantenimientoForm})
#----------------------------------------------------------------------------------------------------------#
#*##---------------- proveedor ------------##

@login_required(None, "", 'login')
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

    return render(request, "proveedor/crear_proveedor.html" , {'proveedor': proveedorForm})

@login_required(None, "", 'login')
def consultar_proveedor (request):
    buscarpornombre_comercial = Buscarpornombre_comercial()
    #buscarporfecha = Buscarporfecha()
    proveedor_p = None

    if request.method == "POST":
        #buscarporfecha = Buscarporfecha(request.POST or None)
        buscarpornombre_comercial = Buscarpornombre_comercial(request.POST or None)
        if buscarpornombre_comercial.is_valid():
            #desde = buscarporfecha.cleaned_data['desde']
            #hasta = buscarporfecha.cleaned_data['hasta']
            nombre_comercial = buscarpornombre_comercial.cleaned_data['nombre_comercial']

            proveedor_p = proveedor.objects.filter(nombre_comercial__startswith=nombre_comercial)
    else:

          proveedor_p = proveedor.objects.all()
    return render(request, "proveedor/consultar_proveedor.html" , {'proveedor_ls': proveedor_p,'buscarpornombre_comercial':buscarpornombre_comercial})


@login_required(None, "", 'login')
def eliminar_proveedor (request,id):
    if request.method == "POST":
        proveedorn = get_object_or_404(proveedor, pk=id)
        proveedorForm = ProveedorForm(request.POST or None, instance=proveedorn)
        if proveedorForm.is_valid():
            proveedorn.estado = 0
            proveedorn.save()
            return redirect('consultar_proveedor')

    else:
        proveedorn = get_object_or_404(proveedor, pk=id)
        proveedorForm = ProveedorForm(request.POST or None, instance=proveedorn)
    return render(request, "proveedor/eliminar_proveedor.html", {'proveedorform': proveedorForm})


@login_required(None, "", 'login')
def modificar_proveedor (request,id):
    if request.method == "POST":
        proveedorn = get_object_or_404(cliente, pk=id)
        proveedorForm = ProveedorForm(request.POST or None, instance=proveedorn)
        if proveedorForm.is_valid():
            proveedorForm.save()
            return redirect('consultar_proveedor')
        else:
            proveedorForm = ProveedorForm(instance=proveedorn)
    else:  ##GET
        proveedorn = get_object_or_404(proveedor, pk=id)
        proveedorForm = ProveedorForm(request.POST or None, instance=proveedorn)

    return render(request, "proveedor/modificar_proveedor.html", {'proveedorform': proveedorForm})
#---------------------------------------------------------------------------------------------------#
##---------------- servicio ------------##


@login_required(None, "", 'login')
def crear_servicio (request):
    if request.method == "POST":
        servicioForm = ServicioForm(request.POST)
        if servicioForm.is_valid():
            servicioForm.save()
            return redirect('consultar_servicio')
        else:
            servicioForm = ServicioForm()
    else:
        servicioForm = ServicioForm()

    return render(request, "servicio/crear_servicio.html" , {'servicio': servicioForm})


@login_required(None, "", 'login')
def consultar_servicio (request):
    buscarpornombre_de_servicios = Buscarpornombre_servicios()
    #buscarporfecha = Buscarporfecha()
    servicio_p = None

    if request.method == "POST":
        #buscarporfecha = Buscarporfecha(request.POST or None)
        buscarpornombre_de_servicios = Buscarpornombre_servicios(request.POST or None)
        if buscarpornombre_de_servicios.is_valid():
            #desde = buscarporfecha.cleaned_data['desde']
            #hasta = buscarporfecha.cleaned_data['hasta']
            nombre_de_servicios = buscarpornombre_de_servicios.cleaned_data['nombre_de_servicios']

            servicio_p = nombre_de_servicios.objects.filter(nombre_de_servicios__startswith=nombre_de_servicios)
    else:

          servicio_p = servicio.objects.all()
    return render(request, "servicio/consultar_servicio.html" , {'servicio_ls': servicio_p,'buscarpornombre_de_servicios':buscarpornombre_de_servicios})

@login_required(None, "", 'login')
def eliminar_servicio (request,id):
    if request.method == "POST":
        servicion = get_object_or_404(servicio, pk=id)
        servicioForm = ServicioForm(request.POST or None, instance=servicion)
        if servicioForm.is_valid():
            servicion.estado = 0
            servicion.save()
            return redirect('consultar_servicio')

    else:
        servicion = get_object_or_404(servicio, pk=id)
        servicioForm = ServicioForm(request.POST or None, instance=servicion)
    return render(request, "servicio/eliminar_servicio.html", {'servicioform': servicioForm})


@login_required(None, "", 'login')
def modificar_servicio (request,id):
    if request.method == "POST":
        servicion = get_object_or_404(servicio, pk=id)
        servicioForm = ServicioForm(request.POST or None, instance=servicion)
        if servicioForm.is_valid():
            servicioForm.save()
            return redirect('consultar_servicio')
        else:
            servicioForm = ServicioForm(instance=servicion)
    else:  ##GET
        servicion = get_object_or_404(servicio, pk=id)
        servicioForm = ServicioForm(request.POST or None, instance=servicion)

    return render(request, "servicio/modificar_servicio.html", {'servicioform': servicioForm})
##TERMINADOS LOS VIEW##
##-------------- devolucion -------------##

@login_required(None, "", 'login')
def crear_devolucion (request):
    if request.method == "POST":
        devolucionForm = DevolucionForm(request.POST)
        if devolucionForm.is_valid():
              devolucionForm.save()
              return redirect('consultar_devolucion')
        else:
            devolucionForm = DevolucionForm()
    else:
        devolucionForm = DevolucionForm()

    return render(request, "devolucion/crear_devolucion.html",{'devolucion': devolucionForm})

@login_required(None, "", 'login')
def consultar_devolucion (request):
    buscarporfecha_devolucion = Buscarporfecha_devolucion()

    devolucion_p = None

    if request.method == "POST":
        buscarporfecha_devolucion = Buscarporfecha_devolucion(request.POST or None)
        if buscarporfecha_devolucion.is_valid():

            fecha_devolucion = buscarporfecha_devolucion.cleaned_data['fecha_devolucion']

            devolucion_p = devolucion.objects.filter(fecha_devolucion__startswith=fecha_devolucion)
    else:
            devolucion_p = devolucion.objects.all()

    return render(request, "devolucion/consultar_devolucion.html", {'devolucion_ls': devolucion_p,'buscarporfecha_devolucion ':buscarporfecha_devolucion} )


@login_required(None, "", 'login')
def eliminar_devolucion (request):
    if request.method == "POST":
        devoluciones = get_object_or_404(devolucion, pk=id)
        devolucionForm = DevolucionForm(request.POST or None, instance=devolucion)
        if devolucionForm.is_valid():
            devoluciones.estado = 0
            devoluciones.save()
            return redirect('consultar_devolucion')
    else:
        devoluciones = get_object_or_404(devolucion, pk=id)
        devolucionForm = DevolucionForm(request.POST or None, instance=devolucion)

    return render(request, "devolucion/eliminar_devolucion.html", {'devolucionForm': devolucionForm})

@login_required(None, "", 'login')
def modificar_devolucion (request):
    if request.method == "POST":
        devoluciones = get_object_or_404(devolucion, pk=id)
        devolucionForm = DevolucionForm(request.POST or None, instance=devoluciones)
        if devolucionForm.is_valid():
            devolucionForm.save()
            return redirect('consultar_devolucion')
        else:
            devolucionForm = DevolucionForm(instance=devoluciones)
    else:
        devoluciones = get_object_or_404(devolucion, pk=id)
        devolucionForm = DevolucionForm(request.POST or None, instance=devoluciones)

    return render(request, "devolucion/modificar_devolucion.html", {'devolucionForm': devolucionForm})





##-------------- factura -------------##

@login_required(None, "", 'login')
def crear_factura (request):
    if request.method == "POST":
        facturaForm = FacturaForm(request.POST)
        if facturaForm.is_valid():
            facturaForm.save()
            return redirect('consultar_factura')
        else:
            facturaForm = FacturaForm()
    else:
        facturaForm = FacturaForm()

    return render(request, "factura/crear_factura.html", {'factura': facturaForm})


@login_required(None, "", 'login')
def consultar_factura (request):
    buscarfecha_ingresoform = Buscarproducto_v()
    factura_p = None

    if request.method == "POST":
        buscarfecha_ingresoform =Buscarproducto_v(request.POST or None)
        if buscarfecha_ingresoform.is_valid():
           # desde = buscarfecha_ingresoform.cleaned_data['desde']
            herencia = buscarfecha_ingresoform.cleaned_data['herencia']

            factura_p = factura.objects.filter(producto_v__descripcion__icontains= herencia)
    else:
        factura_p = factura.objects.all()

    return render(request, "factura/consultar_factura.html", {'factura_ls': factura_p, 'buscarfecha_ingreso':  buscarfecha_ingresoform})


@login_required(None, "", 'login')
def eliminar_factura (request,id):
    if request.method == "POST":
        facturas = get_object_or_404(factura, pk=id)
        facturaForm = FacturaForm(request.POST or None, instance=facturas)
        if facturaForm.is_valid():
            facturas.estado = 0
            facturas.save()
            return redirect('consultar_factura')
    else:
        facturas = get_object_or_404(factura, pk=id)
        facturaForm = FacturaForm(request.POST or None, instance=facturas)

    return render(request, "factura/eliminar_factura.html", {'facturaForm': facturaForm})


@login_required(None, "", 'login')
def modificar_factura (request,id):
    if request.method == "POST":
        facturas =  get_object_or_404(factura, pk=id)
        facturaForm = FacturaForm(request.POST or None, instance=facturas)
        if facturaForm.is_valid():
            facturaForm.save()
            return redirect('consultar_factura')
        else:
            facturas = FacturaForm(instance=facturas)
    else:
        facturas = get_object_or_404(factura, pk=id)
        facturaForm = FacturaForm(request.POST or None, instance=facturas)

    return render(request, "factura/modificar_factura.html", {'facturaForm': facturaForm})





##-------------- producto/ -------------##

@login_required(None, "", 'login')
def crear_producto (request):

    if request.method == "POST":
        productoForm = ProductoForm(request.POST)
        if productoForm.is_valid():
            productoForm.save()
            return redirect('consultar_producto')
        else:
            productoForm = ProductoForm()
    else:
        productoForm = ProductoForm()

    return render(request, "producto/crear_producto.html", {'producto_c': productoForm})

@login_required(None, "", 'login')
def consultar_producto (request):
    buscarfecha_ingresoform = Buscar_por_fecha()
    producto_p = None

    if request.method == "POST":
        buscarfecha_ingresoform = Buscar_por_fecha(request.POST or None)
        if buscarfecha_ingresoform.is_valid():
            desde = buscarfecha_ingresoform.cleaned_data['desde']
            hasta = buscarfecha_ingresoform.cleaned_data['hasta']

            producto_p = producto.objects.filter(fecha_creacion__range=(desde, hasta))
    else:
        producto_p = producto.objects.all()

    return render(request, "producto/consultar_producto.html", {'producto_ls': producto_p, 'buscarfecha_ingreso': buscarfecha_ingresoform})

@login_required(None, "", 'login')
def eliminar_producto (request):
    if request.method == "POST":
        productos = get_object_or_404(producto, pk=id)
        productoForm = ProductoForm(request.POST or None, instance=productos)
        if productoForm.is_valid():
            productos.estado= 0
            productos.save()
            return redirect('consultar_producto')
    else:
        productos = get_object_or_404(producto, pk=id)
        productoForm = ProductoForm(request.POST or None, instance=productos)


    return render(request, "producto/eliminar_producto.html", {'producto': productoForm})



@login_required(None, "", 'login')
def modificar_producto (request):
    if request.method == "POST":
        productos = get_object_or_404(producto, pk=id)
        productoForm = ProductoForm(request.POST or None, instance=productos)
        if productoForm.is_valid():
            productos.save()
            return redirect('consultar_producto')

    else:
        productos = get_object_or_404(producto, pk=id)
        productoForm = ProductoForm(request.POST or None, instance=productos)

    return render(request, "producto/modificar_producto.html", {'producto': productoForm})







##-------------- tipo_de_documento -------------##

@login_required(None, "", 'login')
def crear_tipo_de_documento (request):
    if request.method == "POST":
        tipo_de_documentoForm = Tipo_de_documentoForm(request.POST)
        if tipo_de_documentoForm.is_valid():
            tipo_de_documentoForm.save()
            return redirect('consultar_tipo_de_documento')
        else:
            tipo_de_documentoForm = Tipo_de_documentoForm()
    else:
        tipo_de_documentoForm = Tipo_de_documentoForm()

    return render(request, "tipo_de_documento/crear_tipo_de_documento.html", {'tipo_de_documento' : tipo_de_documentoForm})


@login_required(None, "", 'login')
def consultar_tipo_de_documento (request):
    buscartipo_de_documento = Buscarportipo_de_documento()
    tipo_de_documento_p = None

    if request.method == "POST":
        buscarportipo_de_documento = Buscarportipo_de_documento(request.POST or None)
        if buscarportipo_de_documento.is_valid():
            documento = buscarportipo_de_documento.cleaned_data['tipo_de_documento']

            tipo_de_documento_p = tipo_de_documento.objects.filter(tipo_de_documento__startswith=documento)
    else:
            tipo_de_documento_p = tipo_de_documento.objects.all()

    return render(request, "tipo_de_documento/consultar_tipo_de_documento.html", {'tipo_de_documento_ls': tipo_de_documento_p,'buscarportipo_de_documento':buscartipo_de_documento})


@login_required(None, "", 'login')
def eliminar_tipo_de_documento (request,id):
    if request.method == "POST":
        Tipo_de_documentos = get_object_or_404(tipo_de_documento, pk=id)
        tipo_de_documentoForm = Tipo_de_documentoForm(request.POST or None, instance=Tipo_de_documentos)
        if  tipo_de_documentoForm.is_valid():
            Tipo_de_documentos.estado = 0
            Tipo_de_documentos.save()
            return redirect('consultar_tipo_de_documento')
    else:

        Tipo_de_documentos = get_object_or_404(tipo_de_documento, pk=id)
        tipo_de_documentoForm = Tipo_de_documentoForm(request.POST or None, instance=Tipo_de_documentos)


    return render(request, "tipo_de_documento/eliminar_tipo_de_documento.html", {'tipo_de_documento' : tipo_de_documentoForm})


@login_required(None, "", 'login')
def modificar_tipo_de_documento (request,id):
    if request.method == "POST":
        tipo_de_documentos = get_object_or_404(tipo_de_documento, pk=id)
        tipo_de_documentoForm = Tipo_de_documentoForm(request.POST or None, instance= tipo_de_documentos)
        if  tipo_de_documentoForm.is_valid():
            tipo_de_documentos.save()
            return redirect('consultar_tipo_de_documento')

    else:
        tipo_de_documentos = get_object_or_404(tipo_de_documento, pk=id)
        tipo_de_documentoForm = Tipo_de_documentoForm(request.POST or None, instance=tipo_de_documentos)

    return render(request, "tipo_de_documento/modificar_tipo_de_documento.html", {'tipo_de_documento' : tipo_de_documentoForm})

