from django.db import models
from core.persona.models import Persona


class Cliente(Persona):
    '''
    Campos para el modelo Cliente
    '''
    nit_cliente = models.CharField(verbose_name='Nit',primary_key=True,max_length=10)
    favorito = models.BooleanField(verbose_name='Favorito',default=False)

    '''
    Funcion para la devolución del objeto Cliente
    '''
    def __str__(self):
        return f'{self.nit_cliente} - {self.nombre} {self.apellido}'

    '''
    Configuraciones de la clase Meta
    '''
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'