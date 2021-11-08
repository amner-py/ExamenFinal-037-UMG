from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render,get_object_or_404
from django.urls import reverse_lazy
from core.telefono.models import TipoTelefono,Telefono
from core.telefono.forms import FormTipoTelefono,FormTelefono
from core.cliente.models import Cliente


'''
VISTAS PARA TIPO TELEFONO
'''
class TipoTelefonoList(ListView):
    model = TipoTelefono
    template_name = 'tipo_telefono/list_tipo_telefono.html'


class TipoTelefonoCreate(SuccessMessageMixin,CreateView):
    model = TipoTelefono
    form_class = FormTipoTelefono
    template_name = 'tipo_telefono/add_tipo_telefono.html'
    success_url = reverse_lazy('telefono:addTipoTelefono')
    success_message = 'Ingresado con éxito...'


class TipoTelefonoUpdate(SuccessMessageMixin,UpdateView):
    model = TipoTelefono
    form_class = FormTipoTelefono
    template_name = 'tipo_telefono/edit_tipo_telefono.html'
    success_url =  reverse_lazy('telefono:listTipoTelefono')
    success_message = 'Modificado con éxito...'

    def get(self, request, *args, **kwargs):
        id = self.kwargs.get('pk')
        tipo = get_object_or_404(TipoTelefono,pk=id)
        return render(request,self.template_name,{'tipo':tipo})


class TipoTelefonoDelete(SuccessMessageMixin,DeleteView):
    model = TipoTelefono
    template_name = 'tipo_telefono/delete_tipo_telefono.html'
    success_url = reverse_lazy('telefono:listTipoTelefono')
    success_message = 'Eliminado con éxito...'

    def get(self, request, *args, **kwargs):
        id = self.kwargs.get('pk')
        tipo = get_object_or_404(TipoTelefono,pk=id)
        return render(request,self.template_name,{'tipo':tipo})



'''
VISTAS PARA TELEFONO
'''
class TelefonoList(ListView):
    model = Telefono
    template_name = 'telefono/list_telefono.html'

    def get(self, request, *args, **kwargs):
        nit = self.kwargs.get('pk')
        telefonos = []
        tels = Telefono.objects.all()
        for tel in tels:
            if tel.cliente.nit_cliente == nit:
                telefonos.append(tel)
        return render(request, self.template_name,{'telefonos':telefonos,'nit':nit})

class TelefonoCreate(SuccessMessageMixin,CreateView):
    model = Telefono
    form_class = FormTelefono
    template_name = 'telefono/add_telefono.html'
    success_url = reverse_lazy('cliente:listCliente')
    success_message = 'Ingresado con éxito...'

    def get(self, request, *args, **kwargs):
        tipos = TipoTelefono.objects.all()
        nit = self.kwargs.get('pk')
        return render(request,self.template_name,{'tipos':tipos,'nit':nit})



class TelefonoUpdate(SuccessMessageMixin,UpdateView):
    model = Telefono
    form_class = FormTelefono
    template_name = 'telefono/edit_telefono.html'
    success_url =  reverse_lazy('cliente:listCliente')
    success_message = 'Modificado con éxito...'

    def get(self, request, *args, **kwargs):
        id = self.kwargs.get('pk')
        telefono = get_object_or_404(Telefono,pk=id)
        return render(request,self.template_name,{'telefono':telefono})


class TelefonoDelete(SuccessMessageMixin,DeleteView):
    model = Telefono
    template_name = 'telefono/delete_telefono.html'
    success_url = reverse_lazy('cliente:listCliente')
    success_message = 'Eliminado con éxito...'

    def get(self, request, *args, **kwargs):
        id = self.kwargs.get('pk')
        telefono = get_object_or_404(Telefono,pk=id)
        return render(request,self.template_name,{'telefono':telefono})