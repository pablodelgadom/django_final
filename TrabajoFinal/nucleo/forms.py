from django.forms import widgets
from nucleo.models import Cliente, Especialista
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
            'usuario'
        ]
        labels = {
            'dni': 'DNI',
            'nombre': 'Nombre',
            'apellidos': 'Apellidos',
            'direccion': 'Direccion',
            'fechaNacimiento': 'Fecha de nacimiento',
            'foto': 'Foto',
            'usuario': 'Id de usuario'
        }
        widgets = {
            'dni': forms.TextInput(attrs={'class':'form-control'}), 
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellidos': forms.TextInput(attrs={'class':'form-control'}),
            'direccion': forms.TextInput(attrs={'class':'form-control'}),
            'usuario': forms.Select(attrs={'class':'form-control'}),
        }


class clienteForm(forms.ModelForm):
    
    class Meta:
        model = Cliente

        fields= [
            'dni',
            'nombre',
            'apellidos',
            'direccion',
            'fechaNacimiento',
            'foto',
            'usuario'
        ]
        labels = {
            'dni': 'DNI',
            'nombre': 'Nombre',
            'apellidos': 'Apellidos',
            'direccion': 'Direccion',
            'fechaNacimiento': 'Fecha de nacimiento',
            'foto': 'Foto',
            'biografia': 'Biografia',
            'usuario': 'Id de usuario'
        }
        widgets = {
            'dni': forms.TextInput(attrs={'class':'form-control'}), 
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellidos': forms.TextInput(attrs={'class':'form-control'}),
            'direccion': forms.TextInput(attrs={'class':'form-control'}),
            'usuario': forms.Select(attrs={'class':'form-control'}),
        }