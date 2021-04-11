from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from nucleo import views

app_name = "nucleo"

urlpatterns = [
    path('', views.Portada, name="Portada"),
]