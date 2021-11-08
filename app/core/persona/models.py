from django.db import models
from datetime import date


class Persona(models.Model):
    '''
    Campos para el modelo Persona
    '''
    nombre = models.CharField(verbose_name='Nombre',max_length=50)
    apellido = models.CharField(verbose_name='Apellido',max_length=50)
    genero = models.CharField(verbose_name='Género',max_length=1)
    fecha_nacimiento = models.DateField(verbose_name='Fecha de nacimiento')
    correo = models.CharField(verbose_name='Correo',max_length=100)

    '''
    Funcion para obtener la edad
    '''
    def getEdad(self,fecha_nacimiento):
        fecha_actual =  date.today()
        return fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month,fecha_actual.day) < (fecha_nacimiento.month,fecha_nacimiento.day))

    '''
    Configuración de la clase Meta
    '''
    class Meta:
        abstract = True
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'