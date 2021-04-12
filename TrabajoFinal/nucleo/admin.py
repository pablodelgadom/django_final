from nucleo.models import Cita, Cliente, Especialista, Mensaje
from django.contrib import admin


class ClienteAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Cliente._meta.fields]

class EspecialistaAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Especialista._meta.fields]


class MensajeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Mensaje._meta.fields]

class CitaAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Cita._meta.fields]

# Register your models here.

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Especialista, EspecialistaAdmin)
admin.site.register(Mensaje, MensajeAdmin)
admin.site.register(Cita, CitaAdmin)