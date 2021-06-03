from io import BytesIO
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.views.generic.base import View
from nucleo.decorators import cliente_required, especialista_required
from nucleo.forms import AplazarForm, CitaForm, EditUserForm, LeidoForm, MensajeFormC,MensajeFormE, RellenarForm, UserForm
from nucleo.models import Cita, Mensaje, User
from django.shortcuts import redirect, render
from django.views.generic import CreateView,UpdateView,DeleteView
from django.urls.base import reverse_lazy
from nucleo.decorators import cliente_required, especialista_required
from django.utils.decorators import method_decorator
from reportlab.lib.units import cm
from reportlab.lib import colors
import datetime
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfform
from reportlab.lib.colors import magenta, pink, blue, green, red

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
        form =  CitaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('nucleo:Portada')
    else:
        form = CitaForm()

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

    @method_decorator(cliente_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


def aplazar(request, id_cita):
    cita = Cita.objects.get(id=id_cita)
    if request.method == 'GET':
        form = AplazarForm(instance=cita)
    else:
        form = AplazarForm(request.POST, instance=cita)
        if form.is_valid():
            form.save()
        return redirect('nucleo:Portada')
    return render(request, 'nucleo/citas/create.html', {'form':form})

class aplazarCita(UpdateView):
    model = Cita
    form_class = AplazarForm
    template_name = 'nucleo/citas/create.html'
    success_url = reverse_lazy('nucleo:Portada')

    @method_decorator(especialista_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)



def rellenar(request, id_cita):
    cita = Cita.objects.get(id=id_cita)
    if request.method == 'GET':
        form = RellenarForm(instance=cita)
    else:
        form = RellenarForm(request.POST, instance=cita)
        if form.is_valid():
            form.save()
        return redirect('nucleo:Portada')
    return render(request, 'nucleo/citas/create.html', {'form':form})

class rellenarInforme(UpdateView):
    model = Cita
    form_class = RellenarForm
    template_name = 'nucleo/citas/create.html'
    success_url = reverse_lazy('nucleo:Portada')

    @method_decorator(especialista_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


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


    #Mensajes

def crearMensaje(request):
    if request.method == 'POST':
        form = MensajeFormC(request.POST)
        if form.is_valid():
            form.save()
        return redirect('nucleo:Portada')
    else:
        form = MensajeFormC()

    return render(request, 'nucleo/mensajes/create.html', {'form':form})


@method_decorator(login_required, name='dispatch')
class mensajeCreate(CreateView):
    model = Mensaje
    form_class = MensajeFormC
    template_name = 'nucleo/mensajes/create.html'
    success_url = reverse_lazy('nucleo:Portada')

    def form_valid(self, form):
        # Entramos al if si el usuario autenticado no es admin
        if not self.request.user.is_superuser:

            form.instance.idEmisor = self.request.user # Damos el valor al campo
            form.instance.fecha = datetime.date.today()
            form.instance.leido = False

        return super().form_valid(form)
    
    @method_decorator(cliente_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)




def crearMensajeE(request):
    if request.method == 'POST':
        form = MensajeFormE(request.POST)
        if form.is_valid():
            form.save()
        return redirect('nucleo:Portada')
    else:
        form = MensajeFormE()

    return render(request, 'nucleo/mensajes/createE.html', {'form':form})


@method_decorator(login_required, name='dispatch')
class mensajeCreateE(CreateView):
    model = Mensaje
    form_class = MensajeFormE
    template_name = 'nucleo/mensajes/createE.html'
    success_url = reverse_lazy('nucleo:Portada')

    def form_valid(self, form):
        # Entramos al if si el usuario autenticado no es admin
        if not self.request.user.is_superuser:

            form.instance.idEmisor = self.request.user # Damos el valor al campo
            form.instance.fecha = datetime.date.today()
            form.instance.leido = False

        return super().form_valid(form)

    @method_decorator(especialista_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)



def editarMensaje(request, id_mensaje):
    mensaje = Mensaje.objects.get(id=id_mensaje)
    if request.method == 'GET':
        form = LeidoForm(instance=mensaje)
    else:
        form = LeidoForm(request.POST, instance=mensaje)
        if form.is_valid():
            form.save()
        return redirect('nucleo:Portada')
    return render(request, 'nucleo/mensajes/create.html', {'form':form})

@method_decorator(login_required, name='dispatch')
class mensajeUpdate(UpdateView):
    model = Mensaje
    form_class = LeidoForm
    template_name = 'nucleo/mensajes/create.html'
    success_url = reverse_lazy('nucleo:Portada')
    

@login_required
def recibidos(request, pk):
    mensaje=Mensaje.objects.filter(idReceptor=pk).order_by('-fecha')
    context={'mensajes':mensaje}
    return render(request, 'nucleo/mensajes/recibidos.html',context)

@login_required
def enviados(request, pk):
    mensaje=Mensaje.objects.filter(idEmisor=pk).order_by('-fecha')
    context={'mensajes':mensaje}
    return render(request, 'nucleo/mensajes/enviados.html',context)


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
def pendientes(request, pk):
    cita=Cita.objects.filter(idEspecialista=pk).filter(realizada=False)
    context={'citas':cita}
    return render(request, 'nucleo/citas/updateE.html',context)

@especialista_required
def hoy(request, pk):
    cita=Cita.objects.filter(idEspecialista=pk).filter(fecha=datetime.date.today())
    context={'citas':cita}
    return render(request, 'nucleo/citas/hoy.html',context)

class PDF(View):  
     
    def cabecera(self,pdf):
        #Utilizamos el archivo logo_django.png que está guardado en la carpeta media/imagenes
        archivo_imagen = settings.MEDIA_ROOT+'/img/Portada.png'
        #Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes
        pdf.drawImage(archivo_imagen, 40, 750, 120, 90,preserveAspectRatio=True)
        #Establecemos el tamaño de letra en 16 y el tipo de letra Helvetica
        pdf.setFont("Helvetica", 16)
        #Dibujamos una cadena en la ubicación X,Y especificada
        pdf.drawString(230, 790, u"YO TE AYUDO")
        pdf.setFont("Helvetica", 14)
        pdf.drawString(200, 770, u"REPORTE DE CLIENTE")
         
    def get(self, request, *args, **kwargs):
        #Indicamos el tipo de contenido a devolver, en este caso un pdf
        response = HttpResponse(content_type='application/pdf')
        #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
        buffer = BytesIO()
        #Canvas nos permite hacer el reporte con coordenadas X y Y
        pdf = canvas.Canvas(buffer)
        #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
        self.cabecera(pdf)
        # self.fechas()
        self.tablaCliente(pdf, 600)
        self.tablaCitas(pdf, 200)
        #Con show page hacemos un corte de página para pasar a la siguiente
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response

    def tablaCliente(self,pdf,y):
        usuario = []

        for u in User.objects.all():
            if u.id == self.request.user.id :
                usuario+=u
        #Creamos una tupla de encabezados para neustra tabla
        encabezados = ('DNI', 'Nombre', 'Apellidos', 'Direccion')
        #Creamos una lista de tuplas que van a contener a las personas
        detalles = [(u.dni, u.first_name, u.last_name,u.direccion) for u in usuario]
        #Establecemos el tamaño de cada una de las columnas de la tabla
        detalle_orden = Table([encabezados] + detalles, colWidths=[3 * cm, 5 * cm, 5 * cm, 5 * cm])
        #Aplicamos estilos a las celdas de la tabla
        detalle_orden.setStyle(TableStyle(
            [
                #La primera fila(encabezados) va a estar centrada
                ('ALIGN',(0,0),(3,0),'CENTER'),
                #Los bordes de todas las celdas serán de color negro y con un grosor de 1
                ('GRID', (0, 0), (-1, -1), 1, colors.black), 
                #El tamaño de las letras de cada una de las celdas será de 10
                ('FONTSIZE', (0, 0), (-1, -1), 10),
            ]
        ))
        #Establecemos el tamaño de la hoja que ocupará la tabla 
        detalle_orden.wrapOn(pdf, 800, 600)
        #Definimos la coordenada donde se dibujará la tabla
        detalle_orden.drawOn(pdf, 40,y)


    def tablaCitas(self,pdf,y):
            #Creamos una tupla de encabezados para neustra tabla
            encabezados = ('Fecha', 'Especialista', 'Informe')
            #Creamos una lista de tuplas que van a contener a las personas
            detalles = [(u.fecha, u.idEspecialista,u.informe) for u in Cita.objects.all()]
            #Establecemos el tamaño de cada una de las columnas de la tabla
            detalle_orden = Table([encabezados] + detalles, colWidths=[3 * cm, 5 * cm, 5 * cm, 5 * cm])
            #Aplicamos estilos a las celdas de la tabla
            detalle_orden.setStyle(TableStyle(
                [
                    #La primera fila(encabezados) va a estar centrada
                    ('ALIGN',(0,0),(3,0),'CENTER'),
                    #Los bordes de todas las celdas serán de color negro y con un grosor de 1
                    ('GRID', (0, 0), (-1, -1), 1, colors.black), 
                    #El tamaño de las letras de cada una de las celdas será de 10
                    ('FONTSIZE', (0, 0), (-1, -1), 10),
                ]
            ))
            #Establecemos el tamaño de la hoja que ocupará la tabla 
            detalle_orden.wrapOn(pdf, 800, 600)
            #Definimos la coordenada donde se dibujará la tabla
            detalle_orden.drawOn(pdf, 40,y)

    
    def fechas():
        c = canvas.Canvas('simple_choices.pdf')
    
        c.setFont("Courier", 20)
        c.drawCentredString(300, 700, 'Choices')
        c.setFont("Courier", 14)
        form = c.acroForm
        
        c.drawString(10, 650, 'Choose a letter:')
        options = [('A','Av'),'B',('C','Cv'),('D','Dv'),'E',('F',),('G','Gv')]
        form.choice(name='choice1', tooltip='Field choice1',
                    value='A',
                    x=165, y=645, width=72, height=20,
                    borderColor=magenta, fillColor=pink, 
                    textColor=blue, forceBorder=True, options=options)
    
        c.drawString(10, 600, 'Choose an animal:')
        options = [('Cat', 'cat'), ('Dog', 'dog'), ('Pig', 'pig')]
        form.choice(name='choice2', tooltip='Field choice2',
                    value='Cat',
                    options=options, 
                    x=165, y=595, width=72, height=20,
                    borderStyle='solid', borderWidth=1,
                    forceBorder=True)
        
        c.save()