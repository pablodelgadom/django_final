from django.shortcuts import redirect, render
from django.contrib.auth import logout as do_logout

# Create your views here.


def register_view():
    print()

def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')