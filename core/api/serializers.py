from rest_framework.serializers import ModelSerializer

from atracoes.models import Atracao
from core.models import Pontosturistico
from atracoes.api.serializers import AtracaoSerializer
from comentarios.api.serializers import ComentarioSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer
from enderecos.api.serializers import EnderecoSerializer
from rest_framework import serializers

from enderecos.models import Endereco


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    comentarios = ComentarioSerializer(many=True, read_only=True)
    avaliacoes = AvaliacaoSerializer(many=True, read_only=True)
    endereco = EnderecoSerializer(many=False)
    descricao_completa = serializers.SerializerMethodField()

    class Meta:
        model = Pontosturistico
        fields = (
            'id', 'nome', 'descricao', 'descricao_completa',
            'descricao_completa2', 'aprovado', 'foto', 'atracoes', 'comentarios', 'avaliacoes', 'endereco'
        )
        read_only_fields = ('comentarios', 'avaliacoes')

    def cria_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)

    def create(self, validated_data):
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']
        endereco = validated_data['endereco']
        del validated_data['endereco']
        ponto = Pontosturistico.objects.create(**validated_data)
        self.cria_atracoes(atracoes, ponto)
        ponto.endereco = Endereco.objects.create(**endereco)

        ponto.save()

        return ponto

    def get_descricao_completa(self, obj):
        return f'{obj.nome} - {obj.descricao}'
