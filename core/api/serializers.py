from rest_framework.serializers import ModelSerializer
from core.models import Pontosturistico


class PontoTuristicoSerializer(ModelSerializer):
    class Meta:
        model = Pontosturistico
        fields = ('id', 'nome', 'descricao')
