from nucleo.models import Cliente, Especialista
from django.contrib import admin


class ClienteAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Cliente._meta.fields]

class EspecialistaAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Especialista._meta.fields]


# Register your models here.

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Especialista, EspecialistaAdmin)