from django.urls import path
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
    # Redirige la raíz a la vista con nombre 'home'
    path('', RedirectView.as_view(url='/home/', permanent=True)),
    # Otras URLs de tu aplicación
    path('home/', views.home, name='home'),
    # Otras URLs de tu aplicación
]
