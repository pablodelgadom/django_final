from django.shortcuts import redirect, render
from django.contrib.auth import logout as do_logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.signals import user_logged_out
from django.contrib import messages

# Create your views here.

def register_view():
    print()

def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')

def show_message(sender, user, request, **kwargs):
    # whatever...
    messages.info(request, 'You have been logged out.')

user_logged_out.connect(show_message)

# class UserProfileView(LoginRequiredMixin, UpdateView):
#     model = User
#     form_class = UserProfileForm
#     template_name = 'user/create.html'
#     sucess_url = reverse_lazy('user:user_list')