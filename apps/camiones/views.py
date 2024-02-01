from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import CamionForm
from .models import Camion

# Create your views here.
def lista_camiones(request):
    camiones = Camion.objects.all()
    return render(request, 'camiones/lista_camiones.html', {'camiones': camiones})
def registrar_camion(request):
    if request.method == 'POST':
        form = CamionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_camiones')  # redirige a la lista de camiones o a donde desees
    else:
        form = CamionForm()

    return render(request, 'camiones/registrar_camion.html', {'form': form})
def detalles_camion(request, camion_id):
    camion = get_object_or_404(Camion, id=camion_id)
    return render(request, 'camiones/detalles_camion.html', {'camion': camion})


def editar_camion(request, camion_id):
    camion = get_object_or_404(Camion, id=camion_id)

    if request.method == 'POST':
        form = CamionForm(request.POST, instance=camion)
        if form.is_valid():
            form.save()
            return redirect('lista_camiones')  # Redirige a la lista de camiones o a donde desees
    else:
        form = CamionForm(instance=camion)

    return render(request, 'camiones/editar_camion.html', {'form': form, 'camion': camion})