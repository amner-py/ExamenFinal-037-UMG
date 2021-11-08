from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render,get_object_or_404
from django.urls import reverse_lazy
from core.cliente.models import Cliente
from core.cliente.forms import FormCliente


class ClienteList(ListView):
    model = Cliente
    template_name = 'list_cliente.html'


class ClienteCreate(SuccessMessageMixin,CreateView):
    model = Cliente
    form_class = FormCliente
    template_name = 'add_cliente.html'
    success_url = reverse_lazy('cliente:addCliente')
    success_message = 'Ingresado con éxito...'

    def post(self, request, *args, **kwargs):
        cliente = Cliente()
        cliente.nit_cliente = request.POST.get('nit_cliente')
        cliente.nombre = request.POST.get('nombre')
        cliente.apellido = request.POST.get('apellido')
        cliente.fecha_nacimiento = request.POST.get('fecha_nacimiento')
        cliente.correo = request.POST.get('correo')
        fav = request.POST.get('favorito')
        if fav == 'on':
            cliente.favorito = True
        else:
            cliente.favorito = False
        cliente.genero = request.POST.get('genero')
        cliente.save()
        return render(request,self.template_name, {'msn':'success','clienteNuevo':cliente.nit_cliente})


class ClienteUpdate(SuccessMessageMixin,UpdateView):
    model = Cliente
    form_class = FormCliente
    template_name = 'edit_cliente.html'
    success_url = reverse_lazy('cliente:listCliente')
    success_message = 'Modificado con éxito...'

    def get(self, request, *args, **kwargs):
        id = self.kwargs.get('pk')
        cliente = get_object_or_404(Cliente,pk=id)
        return render(request,self.template_name,{'cliente':cliente})


class ClienteDelete(SuccessMessageMixin,DeleteView):
    model = Cliente
    template_name = 'delete_cliente.html'
    success_url = reverse_lazy('cliente:listCliente')
    success_message = 'Eliminado con éxito...'

    def get(self, request, *args, **kwargs):
        id = self.kwargs.get('pk')
        cliente = get_object_or_404(Cliente,pk=id)
        return render(request,self.template_name,{'cliente':cliente})