from rest_framework.serializers import ModelSerializer
from .models import (
    Avaliacoes, Clientes, Coletas, Enderecos,
    Materiais, MateriaisParceiros, MateriaisPontosColeta, Pagamentos,
    Parceiros, PontosColeta, Solicitacoes, Telefones, Usuarios
)


class AvaliacoesSerializer(ModelSerializer):
    class Meta:
        model = Avaliacoes
        fields = [
            'id',
            'id_parceiros',
            'id_clientes',
            'nota_parceiros',
            'descricao_parceiros',
            'nota_clientes',
            'descricao_clientes',
            'criado_em',
            'atualizado_em',
        ]


class ClientesSerializer(ModelSerializer):
    class Meta:
        model = Clientes
        fiels = [
            'id',
            'id_usuarios',
            'cpf',
            'criado_em',
            'atualizado_em',
        ]


class ColetasSerializer(ModelSerializer):
    class Meta:
        model = Coletas
        fiels = [
            'id',
            'id_clientes',
            'id_parceiros',
            'id_materiais',
            'peso_material',
            'quantidade_material',
            'id_enderecos',
            'id_solicitacoes',
            'id_pagamentos',
            'criado_em',
            'atualizado_em',
        ]


class EnderecosSerializer(ModelSerializer):
    class Meta:
        model = Enderecos
        fiels = [
            'id',
            'cep',
            'estado',
            'cidade',
            'rua',
            'criado_em',
            'atualizado_em',
        ]


class MateriaisSerializer(ModelSerializer):
    class Meta:
        model = Materiais
        fiels = [
            'id',
            'nome',
            'descricao',
            'preco',
            'criado_em',
            'atualizado_em',
        ]


class MateriaisParceirosSerializer(ModelSerializer):
    class Meta:
        model = MateriaisParceiros
        fiels = [
            'id_materiais',
            'id_parceiros',
        ]


class MateriaisPontosColetaSerializer(ModelSerializer):
    class Meta:
        model = MateriaisPontosColeta
        fiels = [
            'id_materiais',
            'id_pontos_coleta',
        ]


class PagamentosSerializer(ModelSerializer):
    class Meta:
        model = Pagamentos
        fiels = [
            'id',
            'valor_pagamento',
            'saldo_pagamento',
            'estado_pagamento',
            'criado_em',
            'atualizado_em',
        ]


class ParceirosSerializer(ModelSerializer):
    class Meta:
        model = Parceiros
        fiels = [
            'id',
            'id_usuarios',
            'cnpj',
            'criado_em',
            'atualizado_em',
        ]


class PontosColetaSerializer(ModelSerializer):
    class Meta:
        model = PontosColeta
        fiels = [
            'id',
            'nome',
            'id_enderecos',
            'descricao',
            'horario_funcionamento',
            'criado_em',
            'atualizado_em',
        ]


class SolicitacoesSerializer(ModelSerializer):
    class Meta:
        model = Solicitacoes
        fiels = [
            'id',
            'estado_solicitacao',
            'observacoes',
            'latitude',
            'longitude',
            'finalizado_em',
            'criado_em',
            'atualizado_em',
        ]


class TelefonesSerializer(ModelSerializer):
    class Meta:
        model = Telefones
        fiels = [
            'id_usuarios',
            'numero',
            'criado_em',
            'atualizado_em',
        ]


class UsuariosSerializer(ModelSerializer):
    class Meta:
        model = Usuarios
        fiels = [
            'id',
            'nome',
            'email',
            'senha',
            'id_endereco',
            'criado_em',
            'atualizado_em',
        ]
