from datetime import date
from django.forms import widgets
from django.http import request
from nucleo.models import Cita, Mensaje, User
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
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
            'direccion': forms.TextInput(attrs={'class':'form-control'}),
        }


class clienteForm(forms.ModelForm):
    
    class Meta:
        model = User

        fields= [
            'dni',
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
            'direccion',
            'fechaNacimiento',
            'biografia',
            'is_cliente',
        ]
        labels = {
            'dni': 'DNI',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'username' : 'Nombre de usuario',
            'email' : 'Email',
            'password' : 'Contraseña',
            'direccion': 'Direccion',
            'fechaNacimiento': 'Fecha de nacimiento',
            'is_cliente' : 'cliente'
        }
        widgets = {
            'dni': forms.TextInput(attrs={'class':'form-control'}), 
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellidos': forms.TextInput(attrs={'class':'form-control'}),
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
            'direccion': forms.TextInput(attrs={'class':'form-control'}),
        }



class EditUserForm(forms.ModelForm):
    
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
        }
        widgets = {
            'dni': forms.TextInput(attrs={'class':'form-control'}), 
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellidos': forms.TextInput(attrs={'class':'form-control'}),
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
            'direccion': forms.TextInput(attrs={'class':'form-control'}),
        }


class CitaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CitaForm, self).__init__(*args, **kwargs)
        self.fields['idEspecialista'].queryset =  User.objects.filter(is_especialista=True)
    
    class Meta:
        model = Cita
        
        fields= [
            'fecha',
            'idCliente',
            'idEspecialista',
            'informe',
            'realizada',
        ]
        labels = {
            'fecha':'Fecha',
            'idCliente':'Cliente',
            'idEspecialista':'Especialista',
            'informe':'Informe',
            'realizada':'Realizada',
        }
        widgets = {
            'fecha': forms.TextInput(attrs={'class':'form-control'}), 
            'idCliente': forms.Select(attrs={'class':'form-control'}),
            'idEspecialista': forms.Select(attrs={'class':'form-control'}),
            'informe': forms.TextInput(attrs={'class':'form-control'}),
        }

class CitaUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Cita
        
        fields= [
            'fecha',
            'informe',
            'realizada',
        ]
        labels = {
            'fecha':'Fecha',
            'informe':'Informe',
            'realizada':'Realizada',
        }
        widgets = {
            'fecha': forms.TextInput(attrs={'class':'form-control'}), 
            'informe': forms.TextInput(attrs={'class':'form-control'}),
        }

class MensajeForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(MensajeForm, self).__init__(*args, **kwargs)
        #self.fields['idEmisor'].queryset =  User.objects.filter(idEmisor=self.kwargs['pk'].nombre)
        #self.fields['idReceptor'].queryset = self.fields['idReceptor'].queryset.exclude(id=current_user.id)

    class Meta:
        model = Mensaje
        
        fields= [
            'idEmisor',
            'idReceptor',
            'fecha',
            'asunto',
            'texto',
            'leido'
        ]
        labels = {
            'idEmisor': 'Emisor',
            'idReceptor' : 'Receptor',
            'fecha' : 'Fecha',
            'asunto' : 'Asunto',
            'texto' : 'Texto',
            
        }
        widgets = {
            'idReceptor': forms.Select(attrs={'class':'form-control'}),
            'fecha': forms.DateInput(attrs={'class':'form-control'}), 
            'asunto': forms.TextInput(attrs={'class':'form-control'}),
            'texto': forms.Textarea(attrs={'class':'form-control'}),
        }

class LeidoForm(forms.ModelForm):
    
    class Meta:

        model = Mensaje
        
        fields= [
            'leido'
        ]

