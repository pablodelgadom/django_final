from nucleo.models import Cita, Cliente, Especialista, Mensaje
from django.contrib import admin


class ClienteAdmin(admin.ModelAdmin):
    list_filter = ('nombre','dni')
    list_display = [field.name for field in Cliente._meta.fields]
    ordering=['id']
    list_per_page=2

class EspecialistaAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Especialista._meta.fields]
    ordering=['id']
    list_per_page=2


class MensajeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Mensaje._meta.fields]
    ordering=['id']
    list_per_page=2

class CitaAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Cita._meta.fields]
    ordering=['id']
    list_per_page=2

# Register your models here.

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Especialista, EspecialistaAdmin)
admin.site.register(Mensaje, MensajeAdmin)
admin.site.register(Cita, CitaAdmin)