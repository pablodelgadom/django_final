from nucleo.models import Cita, Cliente, Especialista, Mensaje
from django.contrib import admin
from django import forms


class ClienteAdminForm(forms.ModelForm):
    def clean_dni(self):
        if len(self.cleaned_data['dni'])<9:
            raise forms.ValidationError('El DNI es demasiado corto')
        else:
            return self.cleaned_data['dni']

class EspecialistaAdminForm(forms.ModelForm):
    def clean_dni(self):
        if len(self.cleaned_data['dni'])<9:
            raise forms.ValidationError('El DNI es demasiado corto')
        else:
            return self.cleaned_data['dni']
            

class CitaInline(admin.StackedInline):
    model=Cita
    max_num=1

class ClienteAdmin(admin.ModelAdmin):
    list_filter = ['nombre']
    list_display = [field.name for field in Cliente._meta.fields]
    ordering=['nombre']
    list_per_page=10
    inlines=[CitaInline,]
    form=ClienteAdminForm

class EspecialistaAdmin(admin.ModelAdmin):
    list_filter = ['nombre']
    list_display = [field.name for field in Especialista._meta.fields]
    ordering=['nombre']
    list_per_page=10
    form=EspecialistaAdminForm


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

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Especialista, EspecialistaAdmin)
admin.site.register(Mensaje, MensajeAdmin)
admin.site.register(Cita, CitaAdmin)