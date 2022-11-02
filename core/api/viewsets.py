from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.models import Pontosturistico
from core.api.serializers import PontoTuristicoSerializer


class PontosTuristicosViewSet(ModelViewSet):

    #queryset = Pontosturistico.objects.all()
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        return Pontosturistico.objects.filter(aprovado=True)

    # def create(self, request, *args, **kwargs):
    #     pass

    # def list(self, request, *args, **kwargs):
    #     ...

    # def destroy(self, request, *args, **kwargs):
    #     pass

    @action(methods=['get'], detail=True)
    def denunciar(self, request, pk=None):
        pass

    @action(methods=['get'], detail=False)
    def teste(self, request):
        return Response({'message': 'action ok'})
