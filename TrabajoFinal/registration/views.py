from django.contrib.auth.models import User
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from registration.forms import UserCreationFormWithEmail, UserProfileForm
from django.shortcuts import redirect, render
from django.contrib.auth import logout as do_logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.signals import user_logged_out
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
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
    # Redireccionamos a la portada
    return redirect('/')


def show_message(sender, user, request, **kwargs):
    # whatever...
    messages.info(request, 'You have been logged out.')
    user_logged_out.connect(show_message)


class UserProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'registration/perfil.html'
    success_url = reverse_lazy('nucleo:indexEspecialistas')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return self.request.user

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de Perfil'
        context['entity'] = 'Perfil'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context