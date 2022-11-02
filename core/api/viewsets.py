from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.models import Pontosturistico
from core.api.serializers import PontoTuristicoSerializer


class PontosTuristicosViewSet(ModelViewSet):

    #queryset = Pontosturistico.objects.all()
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = Pontosturistico.objects.all()
        if id:
            queryset = queryset.filter(id=id)
        if nome:
            queryset = queryset.filter(nome_iexact=nome)
        if descricao:
            queryset = queryset.filter(descricao_iexact=descricao)
        return queryset

    def create(self, request, *args, **kwargs):
        return super(PontosTuristicosViewSet, self).create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super(PontosTuristicosViewSet, self).list(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(PontosTuristicosViewSet, self).destroy(request, *args, **kwargs)

    @action(methods=['get'], detail=True)
    def denunciar(self, request, pk=None):
        pass

    @action(methods=['get'], detail=False)
    def teste(self, request):
        return Response({'message': 'action ok'})
