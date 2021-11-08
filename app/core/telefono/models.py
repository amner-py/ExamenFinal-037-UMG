from django.db import models
from core.cliente.models import Cliente


class TipoTelefono(models.Model):
    '''
    Campos para el modelo TipoTelefono
    '''
    id_tipo_telefono = models.AutoField(primary_key=True)
    tipo = models.CharField(verbose_name='Tipo de telefono',max_length=20)

    '''
    Método str para devolución de objeto
    '''
    def __str__(self):
        return f'{self.tipo}'

    '''
    Configuraciones para la clase Meta
    '''
    class Meta:
        verbose_name = 'Tipo de teléfono'
        verbose_name = 'Tipos de teléfono'


class Telefono(models.Model):
    '''
    Campos para el modelo Telefono
    '''
    num_telefono = models.PositiveIntegerField(verbose_name='Número de teléfono',primary_key=True)
    predeterminado = models.BooleanField(verbose_name='Predeterminado',default=False)
    tipo = models.ForeignKey(TipoTelefono,verbose_name='Tipo',on_delete=models.SET_NULL, blank=True,null=True)
    cliente = models.ForeignKey(Cliente, verbose_name='Cliente', on_delete=models.CASCADE)

    '''
    Método str para devolución de objeto
    '''
    def __str__(self):
        predeterminado = ''
        if self.predeterminado:
            predeterminado = 'Predeterminado'
        return f'{self.num_telefono} - {predeterminado}'

    '''
    Configuraciones para la clase Meta
    '''
    class Meta:
        verbose_name = 'Teléfono'
        verbose_name_plural = 'Telefonos'