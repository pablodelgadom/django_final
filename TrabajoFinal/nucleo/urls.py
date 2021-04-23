from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from nucleo import views

app_name = "nucleo"

urlpatterns = [
    path('', views.Portada, name="Portada"),

    #Especialistas

    path('especialistas/index', views.especialistaList.as_view(), name="indexEspecialistas"),
    path('especialistas/create', views.especialistaCreate.as_view(), name="crearEspecialistas"),
    path('especialistas/update/<int:pk>', views.especialistaUpdate.as_view(), name="editarEspecialistas"),
    path('especialistas/delete/<int:pk>', views.especialistaDelete.as_view(), name="borrarEspecialistas"),

]