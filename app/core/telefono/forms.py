from django import forms
from core.telefono.models import TipoTelefono,Telefono


'''
Formulario para Tipo de Teléfono
'''
class FormTipoTelefono(forms.ModelForm):

    class Meta:
        model = TipoTelefono
        fields = [
            'tipo',
        ]
        labels = {
            'tipo':'Tipo de teléfono',
        }
        widgets = {
            'tipo':forms.TextInput(),
        }


'''
Formulario para Telefono
'''
class FormTelefono(forms.ModelForm):

    class Meta:
        model = Telefono
        fields = [
            'num_telefono',
            'predeterminado',
            'tipo',
            'cliente',
        ]
        labels = {
            'num_telefono':'Número de teléfono',
            'predeterminado':'Predeterminado',
            'tipo':'Tipo de teléfono',
            'cliente':'Cliente',
        }
        widgets = {
            'num_telefono':forms.NumberInput(),
            'predeterminado':forms.CheckboxInput(),
            'tipo':forms.Select(),
            'cliente':forms.Select(),
        }