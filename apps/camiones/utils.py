from .models import Camion, Mantenimiento

def registrar_mantenimiento(camion, datos_formulario):
    mantenimiento = Mantenimiento(**datos_formulario)
    mantenimiento.camion = camion
    mantenimiento.save()

def actualizar_camion(camion, datos_formulario):
    for campo, valor in datos_formulario.items():
        setattr(camion, campo, valor)
    camion.save()
