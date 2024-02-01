from django.shortcuts import render
from django.shortcuts import render, redirect
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
