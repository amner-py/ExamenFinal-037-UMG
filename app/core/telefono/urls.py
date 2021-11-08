from django.urls import path
from core.telefono.views import TipoTelefonoList,TipoTelefonoCreate,TipoTelefonoUpdate,TipoTelefonoDelete,\
    TelefonoList,TelefonoCreate,TelefonoUpdate,TelefonoDelete

app_name='telefono'

urlpatterns = [
    path('tipo/list/',TipoTelefonoList.as_view(),name='listTipoTelefono'),
    path('tipo/add/',TipoTelefonoCreate.as_view(),name='addTipoTelefono'),
    path('tipo/edit/<int:pk>',TipoTelefonoUpdate.as_view(),name='editTipoTelefono'),
    path('tipo/delete/<int:pk>',TipoTelefonoDelete.as_view(),name='deleteTipoTelefono'),
    path('list/<str:pk>',TelefonoList.as_view(),name='listTelefono'),
    path('add/<str:pk>',TelefonoCreate.as_view(),name='addTelefono'),
    path('edit/<int:pk>',TelefonoUpdate.as_view(),name='editTelefono'),
    path('delete/<int:pk>',TelefonoDelete.as_view(),name='deleteTelefono'),
]