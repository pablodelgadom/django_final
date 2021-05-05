from registration.forms import UserCreationFormWithEmail
from django.http import request
from nucleo.forms import EditUserForm, UserForm
from nucleo.models import User
from django.shortcuts import redirect, render
from django.views.generic import CreateView,UpdateView,DeleteView
from django.urls.base import reverse_lazy

# Create your views here.


#Portada

def Portada(request):
    cliente=User.objects.filter(is_cliente=True)#.filter(is_activate=False)
    especialista=User.objects.filter(is_especialista=True)
    context={'especialistas':especialista,
    'clientes':cliente}
    return render(request, 'nucleo/Portada.html',context)


#Especialistas

def crearEspecialistas(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('nucleo:Portada')
    else:
        form = UserForm()

    return render(request, 'nucleo/especialistas/create.html', {'form':form})

class especialistaCreate(CreateView):
    model = User
    form_class = UserForm
    template_name = 'nucleo/especialistas/create.html'
    success_url = reverse_lazy('nucleo:Portada')

def editarEspecialistas(request, id_especialista):
    especialista = User.objects.get(id=id_especialista)
    if request.method == 'GET':
        form = EditUserForm(instance=especialista)
    else:
        form = EditUserForm(request.POST, instance=especialista)
        if form.is_valid():
            form.save()
        return redirect('nucleo:Portada')
    return render(request, 'nucleo/especialistas/create.html', {'form':form})

class especialistaUpdate (UpdateView):
    model = User
    form_class = EditUserForm
    template_name = 'nucleo/especialistas/create.html'
    success_url = reverse_lazy('nucleo:Portada')

def borrarEspecialistas(request, id_especialista):
    especialista = User.objects.get(id=id_especialista)
    especialista.delete()
    return redirect('nucleo:Portada')

class especialistaDelete(DeleteView):
    model = User
    template_name = "nucleo/especialistas/delete.html"
    success_url = reverse_lazy('nucleo:Portada')



#Clientes

def borrarClientes(request, id_especialista):
    especialista = User.objects.get(id=id_especialista)
    especialista.delete()
    return redirect('nucleo:Portada')

class clienteDelete(DeleteView):
    model = User
    template_name = "nucleo/clientes/delete.html"
    success_url = reverse_lazy('nucleo:Portada')



def activar(request, id):
    User.objects.get(id=id).update(is_activate=True)
    return redirect('nucleo:Portada')

# class activado(UpdateView,id):
#     model= User
#     usuario = User.objects.get(id=id)
#     usuario.is_active=True