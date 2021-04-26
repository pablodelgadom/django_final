from django.forms import widgets
from nucleo.models import Especialista
from django import forms

class especialistaForm(forms.ModelForm):
    
    class Meta:
        model = Especialista

        fields= [
            'dni',
            'nombre',
            'apellidos',
            'direccion',
            'fechaNacimiento',
            'foto',
            'biografia',
            'idUsuario'
        ]
        labels = {
            'dni': 'DNI',
            'nombre': 'Nombre',
            'apellidos': 'Apellidos',
            'direccion': 'Direccion',
            'fechaNacimiento': 'Fecha de nacimiento',
            'foto': 'Foto',
            'biografia': 'Biografia',
            'idUsuario': 'Id de usuario'
        }
        widgets = {
            'dni': forms.TextInput(attrs={'class':'form-control'}), 
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellidos': forms.TextInput(attrs={'class':'form-control'}),
            'direccion': forms.TextInput(attrs={'class':'form-control'}),
            'biografia': forms.TextInput(attrs={'class':'form-control'}),
            'idUsuario': forms.Select(attrs={'class':'form-control'}),
        }