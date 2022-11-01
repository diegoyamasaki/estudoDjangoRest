from rest_framework.viewsets import ModelViewSet
from core.models import Pontosturistico
from core.api.serializers import PontoTuristicoSerializer


class PontosTuristicosViewSet(ModelViewSet):

    queryset = Pontosturistico.objects.all()
    serializer_class = PontoTuristicoSerializer
