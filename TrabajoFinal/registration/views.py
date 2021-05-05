from django.contrib.auth.forms import UserChangeForm
from django.views import generic
from nucleo.forms import UserForm, clienteForm
from nucleo.models import User
from registration.forms import ClienteSignUpForm, EditUserProfileForm, UserCreationFormWithEmail, UserProfileForm
from django.shortcuts import redirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth.signals import user_logged_out
from django.contrib import messages
from django.urls.base import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth import login

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
    return redirect('/')+'?logout'


def show_message(sender, user, request, **kwargs):
    # whatever...
    messages.info(request, 'You have been logged out.')
    user_logged_out.connect(show_message)


class UserEditView(generic.UpdateView):
    form_class = EditUserProfileForm
    template_name = 'registration/perfil.html'
    success_url = reverse_lazy('nucleo:Portada')

    def get_object(self):
        return self.request.user



class ClienteSignUpView(CreateView):
    model = User
    form_class = UserCreationFormWithEmail
    template_name = 'registration/registro.html'

    def get_context_data(self, **kwargs):
        kwargs['is_cliente'] = True
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
            user = form.save()
            login(self.request, user)
            return redirect('nucleo:Portada')