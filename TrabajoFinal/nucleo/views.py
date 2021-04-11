from nucleo.models import Cliente
from django.shortcuts import render

# Create your views here.


#Portada

def Portada(request):
    return render(request, 'nucleo/Portada.html')