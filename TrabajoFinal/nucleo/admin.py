from nucleo.models import Cita, Mensaje
from django.contrib import admin


class MensajeAdmin(admin.ModelAdmin):
    list_filter = ['idEmisor']
    list_display = [field.name for field in Mensaje._meta.fields]
    ordering=['idEmisor']
    list_per_page=10

class CitaAdmin(admin.ModelAdmin):
    list_filter = ['fecha']
    list_display = [field.name for field in Cita._meta.fields]
    ordering=['idCliente']
    list_per_page=10

# Register your models here.

admin.site.register(Mensaje, MensajeAdmin)
admin.site.register(Cita, CitaAdmin)