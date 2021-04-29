from nucleo.models import User
from registration.forms import UserCreationFormWithEmail, UserProfileForm
from django.shortcuts import redirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth.signals import user_logged_out
from django.contrib import messages
from django.urls.base import reverse_lazy
from django.views.generic import CreateView, UpdateView

# Create your views here.

class SignupView(CreateView):
    form_class=UserCreationFormWithEmail
    template_name='registration/registro.html'

    def get_success_url(self):
        return reverse_lazy('login')+'?register'

def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    #mensaje
    messages.info(request, "Salistes exitosamente")
    user_logged_out.connect(show_message)
    # Redireccionamos a la portada
    return redirect('/')


def show_message(sender, user, request, **kwargs):
    # whatever...
    messages.info(request, 'You have been logged out.')
    user_logged_out.connect(show_message)


class UserEditView(UpdateView):
    form_class = UserProfileForm
    template_name = 'registration/perfil.html'
    success_url = reverse_lazy('nucleo:Portada')

    def get_object(self, queryset=None):
        return self.request.user