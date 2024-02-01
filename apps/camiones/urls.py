from django.urls import path
from . import views

urlpatterns = [
    path('lista_camiones/', views.lista_camiones, name='lista_camiones'),
    path('registrar_camion/', views.registrar_camion, name='registrar_camion'),
    path('detalles_camion/<int:camion_id>/', views.detalles_camion, name='detalles_camion'),
    path('editar_camion/<int:camion_id>/', views.editar_camion, name='editar_camion'),
]
