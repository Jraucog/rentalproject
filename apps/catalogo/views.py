from django.shortcuts import render
from apps.camiones.models import Camion

def catalogo(request):
    # Obtener todos los camiones
    camiones = Camion.objects.all()

    # Contexto para pasar al template
    context = {
        'title': 'Catálogo de Camiones',
        'camiones': camiones,
    }

    return render(request, 'catalogo/catalogo.html', context)
