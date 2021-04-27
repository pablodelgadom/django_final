from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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