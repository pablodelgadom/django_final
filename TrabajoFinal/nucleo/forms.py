from django.forms import widgets
from nucleo.models import User
from django import forms

class UserForm(forms.ModelForm):
    
    class Meta:
        model = User

        fields= [
            'dni',
            'first_name',
            'last_name',
            'username',
            'password',
            'direccion',
            'foto',
            'fechaNacimiento',
            'biografia',
            'is_especialista',
        ]
        labels = {
            'dni': 'DNI',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'username' : 'Nombre de usuario',
            'pasword' : 'Contraseña',
            'direccion': 'Direccion',
            'foto' : 'foto',
            'fechaNacimiento': 'Fecha de nacimiento',
            'is_especialista' : 'especialista'
        }
        widgets = {
            'dni': forms.TextInput(attrs={'class':'form-control'}), 
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellidos': forms.TextInput(attrs={'class':'form-control'}),
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.TextInput(attrs={'class':'form-control'}),
            'direccion': forms.TextInput(attrs={'class':'form-control'}),
        }


# class clienteForm(forms.ModelForm):
    
#     class Meta:
#         model = Cliente

#         fields= [
#             'dni',
#             'nombre',
#             'apellidos',
#             'direccion',
#             'fechaNacimiento',
#             'foto',
#             'usuario'
#         ]
#         labels = {
#             'dni': 'DNI',
#             'nombre': 'Nombre',
#             'apellidos': 'Apellidos',
#             'direccion': 'Direccion',
#             'fechaNacimiento': 'Fecha de nacimiento',
#             'foto': 'Foto',
#             'biografia': 'Biografia',
#             'usuario': 'Id de usuario'
#         }
#         widgets = {
#             'dni': forms.TextInput(attrs={'class':'form-control'}), 
#             'nombre': forms.TextInput(attrs={'class':'form-control'}),
#             'apellidos': forms.TextInput(attrs={'class':'form-control'}),
#             'direccion': forms.TextInput(attrs={'class':'form-control'}),
#             'usuario': forms.Select(attrs={'class':'form-control'}),
#         }