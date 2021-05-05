from django import forms
from django.forms.fields import BooleanField, FileField
from nucleo.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms.models import ModelForm
from django.db import transaction

class UserCreationFormWithEmail(UserCreationForm):
    dni = forms.TextInput(attrs={'class':'form-control'}), 
    first_name = forms.TextInput(attrs={'class':'form-control'}),
    last_name = forms.TextInput(attrs={'class':'form-control'}),
    username = forms.TextInput(attrs={'class':'form-control'}),
    email = forms.EmailField(required=True,help_text="Requerido. 254 caracteres maximo")
    password = forms.PasswordInput(attrs={'class':'form-control'}),
    direccion = forms.TextInput(attrs={'class':'form-control'}),

    class Meta:
        model=User
        fields=('username','email','password1','password2','dni','first_name', 'last_name', 'fechaNacimiento', 'direccion')

    def save(self, commit=True):
        user = super(UserCreationFormWithEmail, self).save()
        user.email = self.cleaned_data["email"]
        user.dni = self.cleaned_data["dni"]
        user.firs_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.fechaNacimiento = self.cleaned_data["fechaNacimiento"]
        user.direccion = self.cleaned_data["direccion"]
        user.is_cliente = True
        user.is_active= True
        user.save()
        return

    def clean_email(self):
        value=self.cleaned_data['email']
        if User.objects.filter(email=value).exists():
            raise forms.ValidationError("Este email ya esta en uso, prueba con otro")
        return value


class ClienteSignUpForm(UserCreationForm):
    interests = forms.ModelMultipleChoiceField

    class Meta(UserCreationForm.Meta):
        model = User


class UserProfileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['autofocus'] = True

    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'email', 'username'
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su nombre',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese sus apellidos',
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su email',
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su username',
                }
            ),
        }
        exclude = ['user_permissions', 'last_login', 'date_joined', 'is_superuser', 'is_active', 'is_staff', 'groups']

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                pwd = self.cleaned_data['password']
                u = form.save(commit=False)
                if u.pk is None:
                    u.set_password(pwd)
                else:
                    user = User.objects.get(pk=u.pk)
                    if user.password != pwd:
                        u.set_password(pwd)
                u.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data



class EditUserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields=['username','email','dni','first_name', 'last_name', 'fechaNacimiento', 'direccion']