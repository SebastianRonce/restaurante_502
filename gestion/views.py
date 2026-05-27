from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from decimal import Decimal

from .models import Cliente, Empleado, Mesa, Plato, Orden, Factura, DetalleOrden
from .forms import ClienteForm, EmpleadoForm, MesaForm, PlatoForm, OrdenForm, FacturaForm, DetalleOrdenFormSet
from .decorators import rol_requerido


# ═══════════════════════════════════════════════════════
# INICIO — dashboard por rol
# ═══════════════════════════════════════════════════════

@login_required
def inicio(request):
    grupos = list(request.user.groups.values_list('name', flat=True))
    context = {
        'grupos': grupos,
        'total_clientes':  Cliente.objects.count(),
        'total_empleados': Empleado.objects.count(),
        'total_mesas':     Mesa.objects.count(),
        'total_platos':    Plato.objects.count(),
        'total_ordenes':   Orden.objects.count(),
        'total_facturas':  Factura.objects.count(),
        'ordenes_activas':   Orden.objects.filter(estado_orden='Activa').count(),
        'ordenes_pendientes': Orden.objects.exclude(estado_orden='Facturada').exclude(estado_orden='Cancelada').count(),
        'mesas_disponibles': Mesa.objects.filter(estado_mesa='Disponible').count(),
    }
    return render(request, 'gestion/inicio.html', context)


# ═══════════════════════════════════════════════════════
# ACCESO DENEGADO
# ═══════════════════════════════════════════════════════

def acceso_denegado(request):
    return render(request, 'gestion/403.html', status=403)


# ═══════════════════════════════════════════════════════
# CLIENTES — Admin: CRUD | Mesero: solo ver | Cajero: nada
# ═══════════════════════════════════════════════════════

@rol_requerido('administrador', 'mesero')
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'gestion/clientes.html', {'clientes': clientes})


@rol_requerido('administrador')
def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes')
    else:
        form = ClienteForm()
    return render(request, 'gestion/form_cliente.html', {'form': form})


@rol_requerido('administrador')
def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'gestion/form_cliente.html', {'form': form})


@rol_requerido('administrador')
def eliminar_cliente(request, id):
    get_object_or_404(Cliente, id=id).delete()
    return redirect('clientes')


# ═══════════════════════════════════════════════════════
# EMPLEADOS — solo Admin
# ═══════════════════════════════════════════════════════

@rol_requerido('administrador')
def lista_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'gestion/empleados.html', {'empleados': empleados})


@rol_requerido('administrador')
def crear_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('empleados')
    else:
        form = EmpleadoForm()
    return render(request, 'gestion/form_empleado.html', {'form': form})


@rol_requerido('administrador')
def editar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('empleados')
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'gestion/form_empleado.html', {'form': form})


@rol_requerido('administrador')
def eliminar_empleado(request, id):
    get_object_or_404(Empleado, id=id).delete()
    return redirect('empleados')


# ═══════════════════════════════════════════════════════
# MESAS — Admin: CRUD | Mesero: solo ver | Cajero: nada
# ═══════════════════════════════════════════════════════

@rol_requerido('administrador', 'mesero')
def lista_mesas(request):
    mesas = Mesa.objects.all()
    return render(request, 'gestion/mesas.html', {'mesas': mesas})


@rol_requerido('administrador')
def crear_mesa(request):
    if request.method == 'POST':
        form = MesaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mesas')
    else:
        form = MesaForm()
    return render(request, 'gestion/form_mesa.html', {'form': form})


@rol_requerido('administrador')
def editar_mesa(request, id):
    mesa = get_object_or_404(Mesa, id=id)
    if request.method == 'POST':
        form = MesaForm(request.POST, instance=mesa)
        if form.is_valid():
            form.save()
            return redirect('mesas')
    else:
        form = MesaForm(instance=mesa)
    return render(request, 'gestion/form_mesa.html', {'form': form})


@rol_requerido('administrador')
def eliminar_mesa(request, id):
    get_object_or_404(Mesa, id=id).delete()
    return redirect('mesas')


# ═══════════════════════════════════════════════════════
# PLATOS — Admin: CRUD | Mesero: solo ver | Cajero: nada
# ═══════════════════════════════════════════════════════

@rol_requerido('administrador', 'mesero')
def lista_platos(request):
    platos = Plato.objects.all()
    return render(request, 'gestion/platos.html', {'platos': platos})


@rol_requerido('administrador')
def crear_plato(request):
    if request.method == 'POST':
        form = PlatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('platos')
    else:
        form = PlatoForm()
    return render(request, 'gestion/form_plato.html', {'form': form})


@rol_requerido('administrador')
def editar_plato(request, id):
    plato = get_object_or_404(Plato, id=id)
    if request.method == 'POST':
        form = PlatoForm(request.POST, instance=plato)
        if form.is_valid():
            form.save()
            return redirect('platos')
    else:
        form = PlatoForm(instance=plato)
    return render(request, 'gestion/form_plato.html', {'form': form})


@rol_requerido('administrador')
def eliminar_plato(request, id):
    get_object_or_404(Plato, id=id).delete()
    return redirect('platos')


# ═══════════════════════════════════════════════════════
# ÓRDENES — Admin: CRUD | Mesero: crear/editar/ver | Cajero: solo ver
# ═══════════════════════════════════════════════════════

@rol_requerido('administrador', 'mesero', 'cajero')
def lista_ordenes(request):
    grupos = list(request.user.groups.values_list('name', flat=True))
    if 'cajero' in grupos and 'administrador' not in grupos:
        ordenes = Orden.objects.exclude(estado_orden='Facturada').exclude(estado_orden='Cancelada')
    else:
        ordenes = Orden.objects.all()
    return render(request, 'gestion/ordenes.html', {'ordenes': ordenes})


@rol_requerido('administrador', 'mesero')
def crear_orden(request):
    platos = Plato.objects.filter(disponible=True)
    if request.method == 'POST':
        form = OrdenForm(request.POST)
        formset = DetalleOrdenFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            orden = form.save(commit=False)
            orden.total = 0
            orden.save()
            formset.instance = orden
            formset.save()
            return redirect('ordenes')
    else:
        form = OrdenForm()
        formset = DetalleOrdenFormSet()
    return render(request, 'gestion/form_orden.html', {
        'form': form, 'formset': formset, 'platos': platos
    })


@rol_requerido('administrador', 'mesero')
def editar_orden(request, id):
    orden = get_object_or_404(Orden, id=id)
    platos = Plato.objects.filter(disponible=True)
    if request.method == 'POST':
        form = OrdenForm(request.POST, instance=orden)
        formset = DetalleOrdenFormSet(request.POST, instance=orden)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('ordenes')
    else:
        form = OrdenForm(instance=orden)
        formset = DetalleOrdenFormSet(instance=orden)
    return render(request, 'gestion/form_orden.html', {
        'form': form, 'formset': formset, 'platos': platos
    })


@rol_requerido('administrador')
def eliminar_orden(request, id):
    get_object_or_404(Orden, id=id).delete()
    return redirect('ordenes')


# ═══════════════════════════════════════════════════════
# FACTURAS — Admin: ver | Cajero: crear/ver | Mesero: nada
# ═══════════════════════════════════════════════════════

@rol_requerido('administrador', 'cajero')
def lista_facturas(request):
    facturas = Factura.objects.all()
    return render(request, 'gestion/facturas.html', {'facturas': facturas})


@rol_requerido('administrador', 'cajero')
def crear_factura(request):
    if request.method == 'POST':
        form = FacturaForm(request.POST)
        if form.is_valid():
            factura = form.save(commit=False)
            subtotal = factura.orden.total
            impuesto = subtotal * Decimal('0.19')
            factura.subtotal = subtotal
            factura.impuesto = impuesto
            factura.total_factura = subtotal + impuesto
            factura.save()
            return redirect('facturas')
    else:
        form = FacturaForm()
    return render(request, 'gestion/form_factura.html', {'form': form})


# ═══════════════════════════════════════════════════════
# AUTENTICACIÓN
# ═══════════════════════════════════════════════════════

def login_view(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('inicio')
        return render(request, 'gestion/login.html', {'error': 'Usuario o contraseña incorrectos'})
    return render(request, 'gestion/login.html')


def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'gestion/registro.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')
