from django.contrib.admin.views.decorators import staff_member_required
from nucleo.decorators import cliente_required, especialista_required
from django.http import request
from nucleo.forms import CitaForm, CitaUpdateForm, EditUserForm, UserForm
from nucleo.models import Cita, User
from django.shortcuts import redirect, render
from django.views.generic import CreateView,UpdateView,DeleteView
from django.urls.base import reverse_lazy
from nucleo.decorators import cliente_required, especialista_required
from django.utils.decorators import method_decorator
import datetime

# Create your views here.


#Portada

def Portada(request):
    cliente=User.objects.filter(is_cliente=True)#.filter(is_activate=False)
    especialista=User.objects.filter(is_especialista=True)
    cita=Cita.objects.filter(realizada=False)
    context={'especialistas':especialista,
    'clientes':cliente,
    'citas':cita}
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

@method_decorator(staff_member_required, name='dispatch')
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

@method_decorator(staff_member_required, name='dispatch')
class especialistaUpdate (UpdateView):
    model = User
    form_class = EditUserForm
    template_name = 'nucleo/especialistas/create.html'
    success_url = reverse_lazy('nucleo:Portada')

def borrarEspecialistas(request, id_especialista):
    especialista = User.objects.get(id=id_especialista)
    especialista.delete()
    return redirect('nucleo:Portada')

@method_decorator(staff_member_required, name='dispatch')
class especialistaDelete(DeleteView):
    model = User
    template_name = "nucleo/especialistas/delete.html"
    success_url = reverse_lazy('nucleo:Portada')



#Clientes

def borrarClientes(request, id_especialista):
    especialista = User.objects.get(id=id_especialista)
    especialista.delete()
    return redirect('nucleo:Portada')

@method_decorator(staff_member_required, name='dispatch')
class clienteDelete(DeleteView):
    model = User
    template_name = "nucleo/clientes/delete.html"
    success_url = reverse_lazy('nucleo:Portada')


#Citas

def crearCitas(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('nucleo:Portada')
    else:
        form = UserForm()

    return render(request, 'nucleo/citas/create.html', {'form':form})

class citaCreate(CreateView):
    model = Cita
    form_class = CitaForm
    template_name = 'nucleo/citas/create.html'
    success_url = reverse_lazy('nucleo:Portada')

    @method_decorator(cliente_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


def editarCitas(request, id_cita):
    cita = Cita.objects.get(id=id_cita)
    if request.method == 'GET':
        form = EditUserForm(instance=cita)
    else:
        form = CitaForm(request.POST, instance=cita)
        if form.is_valid():
            form.save()
        return redirect('nucleo:Portada')
    return render(request, 'nucleo/citas/create.html', {'form':form})

class citaUpdate(UpdateView):
    model = Cita
    form_class = CitaForm
    template_name = 'nucleo/citas/create.html'
    success_url = reverse_lazy('nucleo:Portada')




def editarCitasE(request, id_cita):
    cita = Cita.objects.get(id=id_cita)
    if request.method == 'GET':
        form = EditUserForm(instance=cita)
    else:
        form = CitaUpdateForm(request.POST, instance=cita)
        if form.is_valid():
            form.save()
        return redirect('nucleo:Portada')
    return render(request, 'nucleo/citas/create.html', {'form':form})

class citaUpdateE(UpdateView):
    model = Cita
    form_class = CitaUpdateForm
    template_name = 'nucleo/citas/create.html'
    success_url = reverse_lazy('nucleo:Portada')


def borrarCitas(request, id_cita):
    cita = Cita.objects.get(id=id_cita)
    cita.delete()
    return redirect('nucleo:Portada')

class citaDelete(DeleteView):
    model = Cita
    template_name = "nucleo/citas/delete.html"
    success_url = reverse_lazy('nucleo:Portada')

    @method_decorator(cliente_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

@cliente_required
def historialC(request, pk):
    cita=Cita.objects.filter(idCliente=pk).filter(realizada=True)
    context={'citas':cita}
    return render(request, 'nucleo/citas/historial.html',context)

@especialista_required
def historialE(request, pk):
    cita=Cita.objects.filter(idCliente=pk).filter(idEspecialista=request.user.id).filter(realizada=True)
    context={'citas':cita}
    return render(request, 'nucleo/citas/historial.html',context)

@cliente_required
def CRUD(request, pk):
    cita=Cita.objects.filter(idCliente=pk).filter(realizada=False)
    context={'citas':cita}
    return render(request, 'nucleo/citas/pendientes.html',context)

@especialista_required
def hoy(request, pk):
    cita=Cita.objects.filter(idEspecialista=pk).filter(fecha=datetime.date.today())
    context={'citas':cita}
    return render(request, 'nucleo/citas/hoy.html',context)