from django.urls import path
from . import views

urlpatterns = [
    path('lista_camiones/', views.lista_camiones, name='lista_camiones'),
    path('registrar_camion/', views.registrar_camion, name='registrar_camion'),
]
