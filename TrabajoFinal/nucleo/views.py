from django.shortcuts import render

# Create your views here.


#Portada

def Portada(request):
    noticias=Noticia.objects.all()
    data={'noticias':noticias}
    return render(request, 'nucleo/Portada.html', data)