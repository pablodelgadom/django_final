from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth import logout as do_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as do_login

# Create your views here.


# def login(request):
#     # Creamos el formulario de autenticación vacío
#     form = AuthenticationForm()
#     if request.method == "POST":
#         # Añadimos los datos recibidos al formulario
#         form = AuthenticationForm(data=request.POST)
#         # Si el formulario es válido...
#         if form.is_valid():
#             # Recuperamos las credenciales validadas
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']

#             # Verificamos las credenciales del usuario
#             user = authenticate(username=username, password=password)

#             # Si existe un usuario con ese nombre y contraseña
#             if user is not None:
#                 # Hacemos el login manualmente
#                 do_login(request, user)
#                 # Y le redireccionamos a la portada
#                 return redirect('/')

#     # Si llegamos al final renderizamos el formulario
#     return render(request, "users/login.html", {'form': form})

def register_view():
    print()

def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')