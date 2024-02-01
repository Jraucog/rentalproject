from django.core.validators import RegexValidator
from django.db import models

class Camion(models.Model):
    ESTADO_CHOICES = [
        ('Disponible', 'Disponible'),
        ('Arrendado', 'Arrendado'),
        ('En Mantenimiento', 'En Mantenimiento'),
        ('Siniestrado', 'Siniestrado'),
        ('En Revisión', 'En Revisión'),
        # Agrega más opciones según sea necesario
    ]
    FLOTA_CHOICES = [
        ('ALJIBE', 'ALJIBE'),
        ('SUPERSUCKER', 'SUPERSUCKER'),
        # Agrega más opciones según sea necesario
    ]
    # Datos para el camión
    centro_costo = models.IntegerField(verbose_name='Centro De Costo', null=True)
    año = models.PositiveIntegerField(verbose_name='Año')
    estado = models.CharField(max_length=50, choices=ESTADO_CHOICES, default='Disponible', verbose_name='Estado')
    ppu = models.CharField(
        max_length=10, verbose_name='PPU', default='AAAA-00', unique=True,
        validators=[
            RegexValidator(
                regex=r'^[A-Z]{4}-[0-9]{2}$',
                message='Formato de PPU no válido. Ejemplo: ABCD-18'
            )
        ]
    )
    marca = models.CharField(max_length=100, verbose_name='Marca')
    modelo = models.CharField(max_length=100, verbose_name='Modelo')
    vin = models.CharField(max_length=255, verbose_name='VIN')
    kilometraje = models.PositiveIntegerField(verbose_name='Kilometraje')
    descripcion = models.CharField(max_length=255, verbose_name='Descripción', blank=True)
    numero_motor = models.IntegerField(verbose_name='Número De Motor', null=True, blank=True)
    flota = models.CharField(max_length=50, choices=FLOTA_CHOICES, verbose_name='Flota', default='none')

    def __str__(self):
        return self.modelo
