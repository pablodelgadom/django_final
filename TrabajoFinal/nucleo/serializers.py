from nucleo.models import Cita
from rest_framework import serializers


class CitasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cita
        fields= ['fecha','idEspecialista','informe']
