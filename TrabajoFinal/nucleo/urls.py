from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from nucleo import views
from nucleo.decorators import cliente_required

app_name = "nucleo"

urlpatterns = [
    path('', views.Portada, name="Portada"),

    #Especialistas

    path('especialistas/create', views.especialistaCreate.as_view(), name="crearEspecialistas"),
    path('especialistas/update/<int:pk>', views.especialistaUpdate.as_view(), name="editarEspecialistas"),
    path('especialistas/delete/<int:pk>', views.especialistaDelete.as_view(), name="borrarEspecialistas"),

    #Clientes

    path('clientes/delete/<int:pk>', views.clienteDelete.as_view(), name="borrarClientes"),


    #Citas

    path('citas/pendientes/<int:pk>', views.CRUD, name="CRUD"),
    path('citas/historial/<int:pk>', views.historialC, name="historialC"),
    path('citas/historialE/<int:pk>', views.historialE, name="historialE"),
    path('citas/create', views.citaCreate.as_view(), name="crearCitas"),
    path('citas/update/<int:pk>', views.citaUpdate.as_view(), name="editarCitas"),
    path('citas/delete/<int:pk>', views.citaDelete.as_view(), name="borrarCitas"),


]