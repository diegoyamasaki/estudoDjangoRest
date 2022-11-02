from rest_framework.serializers import ModelSerializer
from core.models import Pontosturistico
from atracoes.api.serializers import AtracaoSerializer
from comentarios.api.serializers import ComentarioSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer
from enderecos.api.serializers import EnderecoSerializer
from rest_framework import serializers


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True, read_only=True)
    comentarios = ComentarioSerializer(many=True)
    avaliacoes = AvaliacaoSerializer(many=True)
    endereco = EnderecoSerializer(many=False)
    descricao_completa = serializers.SerializerMethodField()

    class Meta:
        model = Pontosturistico
        fields = ('id', 'nome', 'descricao', 'descricao_completa', 'descricao_completa2', 'aprovado', 'foto', 'atracoes', 'comentarios', 'avaliacoes', 'endereco')

    def get_descricao_completa(self, obj):
        return f'{obj.nome} - {obj.descricao}'
