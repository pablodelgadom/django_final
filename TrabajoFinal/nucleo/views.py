from nucleo.forms import especialistaForm
from nucleo.models import Cliente, Especialista
from django.shortcuts import redirect, render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls.base import reverse_lazy

# Create your views here.


#Portada

def Portada(request):
    cliente=Cliente.objects.all()
    especialista=Especialista.objects.all()
    context={'especialistas':especialista,
    'clientes':cliente}
    return render(request, 'nucleo/Portada.html',context)


#Especialistas

def indexEspecialistas(request):
    especialista=Especialista.objects.all()
    context={'especialistas':especialista}
    return render(request, 'nucleo/especialistas/index.html',context)

class especialistaList(ListView):
    model = Especialista
    template_name= 'nucleo/especialistas/index.html'


def crearEspecialistas(request):
    if request.method == 'POST':
        form = especialistaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('especialistas:indexEspecialistas')
    else:
        form = especialistaForm()

    return render(request, 'nucleo/especialistas/create.html', {'form':form})

class especialistaCreate(CreateView):
    model = Especialista
    form_class = especialistaForm
    template_name = 'nucleo/especialistas/create.html'
    success_url = reverse_lazy('nucleo:indexEspecialistas')

def editarEspecialistas(request, id_especialista):
    especialista = Especialista.objects.get(id=id_especialista)
    if request.method == 'GET':
        form = especialistaForm(instance=especialista)
    else:
        form = especialistaForm(request.POST, instance=especialista)
        if form.is_valid():
            form.save()
        return redirect('especialista:especialistaList')
    return render(request, 'nucleo/especialistas/create.html', {'form':form})

class especialistaUpdate (UpdateView):
    model = Especialista
    form_class = especialistaForm
    template_name = 'nucleo/especialistas/create.html'
    success_url = reverse_lazy('nucleo:indexEspecialistas')

def borrarEspecialistas(request, id_especialista):
    especialista = Especialista.objects.get(id=id_especialista)
    if request.method == 'POST':
        especialista.delete()
        return redirect('especialista:especialistaList')
    return render(request, 'nucleo/especialistas/delete.html', {'especialista':especialista})

class especialistaDelete(DeleteView):
    model = Especialista
    template_name = 'nucleo/especialistas/delete.html'
    success_url = reverse_lazy('nucleo:indexEspecialistas')