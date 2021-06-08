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

    path('citas/hoy/<int:pk>', views.hoy, name="hoy"),
    path('citas/pendientes/<int:pk>', views.CRUD, name="CRUD"),
    path('citas/updateE/<int:pk>', views.pendientes, name="pendientes"),
    path('citas/historial/<int:pk>', views.historialC, name="historialC"),
    path('citas/historialE/<int:pk>', views.historialE, name="historialE"),
    path('citas/create', views.citaCreate.as_view(), name="crearCitas"),
    path('citas/update/<int:pk>', views.citaUpdate.as_view(), name="editarCitas"),
    path('citas/update/<int:pk>/AplazarE', views.aplazarCita.as_view(), name="aplazar"),
    path('citas/update/<int:pk>/RellenarE', views.rellenarInforme.as_view(), name="rellenar"),
    path('citas/delete/<int:pk>', views.citaDelete.as_view(), name="borrarCitas"),


    #Mensajes

    path('mensajes/create', views.mensajeCreate.as_view(), name="crearMensajes"),
    path('mensajes/createE', views.mensajeCreateE.as_view(), name="crearMensajesE"),
    path('mensajes/recibidos/<int:pk>', views.recibidos, name="recibidos"),
    path('mensajes/enviados/<int:pk>', views.enviados, name="enviados"),
    path('mensajes/update/<int:pk>', views.mensajeUpdate.as_view(), name="editarMensajes"),

    #pdf

    path('cliente/pdf/<int:pk>', views.PDF.as_view(), name="informe_pdf"),
    path('pdf/form', views.crearPDF, name="crearPDF"),

    #API
    path('api/citas', views.Citas_APIView.as_view()),
    path('api/citas/<int:pk>', views.Citas_APIView_Detail.as_view()),
    path('api/token', views.TestView.as_view())
    
]