from django import forms
from core.cliente.models import Cliente


class FormCliente(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = [
            'nit_cliente',
            'favorito',
            'nombre',
            'apellido',
            'genero',
            'fecha_nacimiento',
            'correo',
        ]
        labels = {
            'nit_cliente':'Nit',
            'favorito':'Favorito',
            'nombre':'Nombre',
            'apellido':'Apellido',
            'genero':'Género',
            'fecha_nacimiento':'Fecha de nacimiento',
            'correo':'Correo',
        }
        widgets = {
            'nit_cliente':forms.TextInput(),
            'favorito':forms.CheckboxInput(),
            'nombre':forms.TextInput(),
            'apellido':forms.TextInput(),
            'genero':forms.CheckboxInput(),
            'fecha_nacimiento':forms.DateInput(),
            'correo':forms.EmailInput(),
        }