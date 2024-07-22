from django import forms
from .models import Camion, Mantenimiento
from django.forms import ModelForm, DateInput

class CamionForm(forms.ModelForm):
    class Meta:
        model = Camion
        fields = ['centro_costo', 'descripcion', 'año', 'estado', 'ppu', 'numero_motor', 'marca', 'modelo', 'kilometraje', 'vin', 'flota']

    def clean_ppu(self):
        # Validación adicional para PPU si es necesario
        ppu = self.cleaned_data.get('ppu')
        # Agrega tu lógica de validación aquí si es necesario
        return ppu

class CamionForm(forms.ModelForm):
    class Meta:
        model = Camion
        fields = ['centro_costo', 'descripcion', 'año', 'estado', 'ppu', 'numero_motor', 'marca', 'modelo', 'kilometraje', 'vin', 'flota']

    def clean_ppu(self):
        # Validación adicional para PPU si es necesario
        ppu = self.cleaned_data.get('ppu')
        # Agrega tu lógica de validación aquí si es necesario
        return ppu



class MantenimientoForm(forms.ModelForm):
    class Meta:
        model = Mantenimiento
        fields = ['tipo', 'descripcion']
        widgets = {
            'fecha': DateInput(attrs={'type': 'date'}), # <-- Se agrega el widget DateInput
        }
