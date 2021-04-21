from nucleo.models import Cliente
from django.shortcuts import render

# Create your views here.


#Portada

def Portada(request):
    cliente=Cliente.objects.all().order_by('nombre')
    context={'clientes':cliente}
    return render(request, 'nucleo/Portada.html',context)
