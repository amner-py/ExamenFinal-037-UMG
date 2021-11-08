from django.contrib import admin
from core.telefono.models import Telefono,TipoTelefono


class TipoTelefonoAdmin(admin.ModelAdmin):
    list_display = ['tipo']
    list_filter = []
    list_editable = []
    list_per_page = 10
    search_fields = ['tipo']


class TelefonoAdmin(admin.ModelAdmin):
    list_display = ['num_telefono', 'predeterminado', 'tipo']
    list_filter = ['predeterminado','tipo']
    list_editable = ['predeterminado']
    list_per_page = 10
    search_fields = ['num_telefono', 'cliente']


admin.site.register(Telefono,TelefonoAdmin)
admin.site.register(TipoTelefono,TipoTelefonoAdmin)