from django.shortcuts import redirect, render
from django.contrib.auth import logout as do_logout
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def register_view():
    print()

def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')


# class UserProfileView(LoginRequiredMixin, UpdateView):
#     model = User
#     form_class = UserProfileForm
#     template_name = 'user/create.html'
#     sucess_url = reverse_lazy('user:user_list')