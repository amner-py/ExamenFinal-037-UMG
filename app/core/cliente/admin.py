from django.contrib import admin
from core.cliente.models import Cliente
from core.telefono.models import Telefono


class TelefonoInline(admin.TabularInline):
    model = Telefono


class ClienteAdmin(admin.ModelAdmin):
    inlines = [TelefonoInline]
    list_display = ['nit_cliente', 'nombre', 'apellido', 'favorito', 'fecha_nacimiento']
    list_filter = ['favorito']
    list_editable = ['nombre','apellido','favorito','fecha_nacimiento']
    list_per_page = 10
    search_fields = ['nit_cliente', 'nombre','apellido','fecha_nacimiento']


admin.site.register(Cliente,ClienteAdmin)