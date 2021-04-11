from typing import TextIO
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Cliente(models.Model):
    dni=models.CharField(max_length=10, null=False, blank=False)
    nombre=models.CharField(max_length=30, null=False, blank=False)
    apellidos=models.CharField(max_length=50, null=False, blank=False)
    direccion=models.CharField(max_length=100, null=False, blank=False)
    fechaNacimiento=models.DateField(verbose_name="Fecha de Nacimiento", null=False)
    foto=models.ImageField
    idUsuario=models.ForeignKey(User, on_delete=models.CASCADE, max_length=11, null=False)

    class Meta:
        verbose_name="Cliente"
        verbose_name_plural="Clientes"

    def __str__(self):
        return self.nombre+" "+self.apellidos

class Especialista(models.Model):
    dni=models.CharField(max_length=10, null=False, blank=False)
    nombre=models.CharField(max_length=30, null=False, blank=False)
    apellidos=models.CharField(max_length=50, null=False, blank=False)
    direccion=models.CharField(max_length=100, null=False, blank=False)
    fechaNacimiento=models.DateField(verbose_name="Fecha de Nacimiento", null=False)
    foto=models.ImageField(upload_to='nucleo/static/img',verbose_name="imagen", null=False)
    biografia=models.CharField(max_length=255, null=False, blank=False)
    idUsuario=models.ForeignKey(User, on_delete=models.CASCADE, max_length=11, null=False)

    class Meta:
        verbose_name="Especialista"
        verbose_name_plural="Especialistas"

    def __str__(self):
        return self.nombre+" "+self.apellidos


class Cita(models.Model):
    fecha=models.DateField(verbose_name="Fecha", null=False)
    idCliente=models.ForeignKey(Cliente, on_delete=models.CASCADE, null=False)
    idEspecialista=models.ForeignKey(Especialista, on_delete=models.CASCADE, null=False)
    informe=models.TextField(null=False, blank=False)
    realizada=models.BooleanField(null=False, blank=False)

    class Meta:
        verbose_name="Cita"
        verbose_name_plural="Citas"

    def __str__(self):
        return self.fecha


class Mensaje(models.Model):
    idEmisor=models.ForeignKey(User, on_delete=models.CASCADE, related_name='emisor', max_length=11, null=False)
    idReceptor=models.ForeignKey(User, on_delete=models.CASCADE, related_name='receptor', max_length=11, null=False)
    fecha=models.DateField(verbose_name="Fecha", null=False)
    asunto=models.CharField(max_length=50, null=False, blank=False)
    texto=models.TextField(null=False, blank=False)
    leido=models.BooleanField(null=False, blank=False)


    class Meta:
        verbose_name="Mensaje"
        verbose_name_plural="Mensajes"

    def __str__(self):
        return self.asunto