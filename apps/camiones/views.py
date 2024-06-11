from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import CamionForm, MantenimientoForm
from .utils import registrar_mantenimiento, actualizar_camion
from .models import Camion, Mantenimiento
# Listado de camiones
def lista_camiones(request):
    camiones = Camion.objects.all()
    return render(request, 'camiones/lista_camiones.html', {'camiones': camiones})

# Registro de camión
def registrar_camion(request):
    if request.method == 'POST':
        form = CamionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_camiones')
    else:
        form = CamionForm()
    return render(request, 'camiones/registrar_camion.html', {'form': form})

# Detalles de camión
def detalles_camion(request, camion_id):
    camion = get_object_or_404(Camion, id=camion_id)
    return render(request, 'camiones/detalles_camion.html', {'camion': camion})

# Edición de camión
def editar_camion(request, camion_id):
    camion = get_object_or_404(Camion, id=camion_id)
    if request.method == 'POST':
        form = CamionForm(request.POST, instance=camion)
        if form.is_valid():
            actualizar_camion(camion, form.cleaned_data)
            return redirect('lista_camiones')
    else:
        form = CamionForm(instance=camion)
    return render(request, 'camiones/editar_camion.html', {'form': form, 'camion': camion})

# Programación de mantenimiento
def programar_mantenimiento(request, camion_id):
    camion = get_object_or_404(Camion, id=camion_id)
    if request.method == 'POST':
        form = MantenimientoForm(request.POST)
        if form.is_valid():
            registrar_mantenimiento(camion, form.cleaned_data)
            return redirect('lista_camiones')
    else:
        form = MantenimientoForm()
    return render(request, 'camiones/programar_mantenimiento.html', {'form': form, 'camion': camion})
