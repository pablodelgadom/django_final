from nucleo.models import Cita,User
from rest_framework import serializers


class CitasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cita
        fields= ['fecha','idEspecialista','informe']
        depth = 3

class EspecialistasSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= ['id','nombre']
