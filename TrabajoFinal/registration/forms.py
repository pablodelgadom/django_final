from django import forms
from nucleo.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import ModelForm

class UserCreationFormWithEmail(UserCreationForm):
    email=forms.EmailField(required=True,help_text="Requerido. 254 caracteres maximo")

    class Meta:
        model=User
        fields=('username','password1','password2','email')

    def save(self, commit=True):
        user = super(UserCreationFormWithEmail, self).save()
        user.email = self.cleaned_data["email"]
        user.save()
        return

    def clean_email(self):
        value=self.cleaned_data['email']
        if User.objects.filter(email=value).exists():
            raise forms.ValidationError("Este email ya esta en uso, prueba con otro")
        return value



class UserProfileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['autofocus'] = True

    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'email', 'username', 'password'
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
            'password': forms.PasswordInput(render_value=True,
                                            attrs={
                                                'placeholder': 'Ingrese su password',
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
