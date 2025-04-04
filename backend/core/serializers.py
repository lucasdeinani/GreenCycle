from rest_framework.serializers import (
    ModelSerializer, CharField, PrimaryKeyRelatedField, DateField
)
from .models import (
    Avaliacoes, Clientes, Coletas, Enderecos,
    Materiais, MateriaisParceiros, MateriaisPontosColeta, Pagamentos,
    Parceiros, PontosColeta, Solicitacoes, Telefones, Usuarios
)
from django.core.validators import MinLengthValidator
from .mixins import (
    ValidacaoCFPMixin,
    ValidacaoCNPJMixin
)
# from django.contrib.auth.hashers import make_password


class UsuarioCreateSerializer(ModelSerializer):
    senha = CharField(
        write_only=True,
        required=True,
        validators=[MinLengthValidator(8)],
        style={'input_type': 'password'}
    )

    class Meta:
        model = Usuarios
        fields = [
            'id',
            'usuario',
            'nome',
            'email',
            'senha',
            'id_endereco',
            'criado_em',
            'atualizado_em',
        ]
        extra_kwargs = {
            'senha': {'write_only': True},
            'email': {'required': True}
        }

    def create(self, validated_data):
        # Criptografa a senha antes de salvar
        # validated_data['senha'] = make_password(validated_data['senha'])

        usuario = Usuarios(**validated_data)
        usuario.save()
        return usuario


class ClienteComUsuarioCreateSerializer(ValidacaoCFPMixin, ModelSerializer):
    nome = CharField(write_only=True, max_length=100)
    usuario = CharField(
        write_only=True,
        max_length=100,
        required=True
    )
    email = CharField(
        write_only=True,
        max_length=100,
        required=False,
        allow_null=True
    )
    senha = CharField(
        write_only=True,
        required=True,
        validators=[MinLengthValidator(8)],
        style={'input_type': 'password'}
    )
    id_endereco = PrimaryKeyRelatedField(
        queryset=Enderecos.objects.all(),
        write_only=True,
        required=False,
        allow_null=True
    )
    id_usuarios = PrimaryKeyRelatedField(read_only=True)
    data_nascimento = DateField()
    sexo = CharField(max_length=1)

    class Meta:
        model = Clientes
        fields = [
            'id',               # Campo do cliente
            'id_usuarios',      # Campo do usuário
            'usuario',          # Campo do usuário
            'cpf',              # Campo do cliente
            'data_nascimento',  # Campo do cliente
            'sexo',             # Campo do cliente
            'criado_em',        # Campo do cliente / usuário
            'atualizado_em',    # Campo do cliente / usuário
            'nome',             # Campo do usuário
            'email',            # Campo do usuário
            'senha',            # Campo do usuário
            'id_endereco'       # Campo do usuário
        ]
        read_only_fields = [
            'id',
            'id_usuarios',
            'criado_em',
            'atualizado_em'
        ]

    def validate_cpf(self, value):
        if value:
            return self.validar_cpf(value)
        return value

    def create(self, validated_data):
        # Extrai os dados do usuário
        usuario_data = {
            'nome': validated_data.pop('nome'),
            'usuario': validated_data.pop('usuario'),
            'email': validated_data.pop('email', None),
            'senha': validated_data.pop('senha'),
            'id_endereco': validated_data.pop('id_endereco', None)
        }

        # Cria o usuário primeiro
        usuario = Usuarios.objects.create(**usuario_data)

        # Cria o cliente vinculado ao usuário
        cliente = Clientes.objects.create(
            id_usuarios=usuario,
            **validated_data
        )

        return cliente

    def update(self, instance, validated_data):
        # Remove campos do usuário que não devem ser atualizados aqui
        validated_data.pop('nome', None)
        validated_data.pop('usuario', None)
        validated_data.pop('email', None)
        validated_data.pop('senha', None)
        validated_data.pop('id_endereco', None)

        return super().update(instance, validated_data)


class ClienteComUsuarioUpdateSerializer(ValidacaoCFPMixin, ModelSerializer):
    nome = CharField(required=False)
    usuario = CharField(
        write_only=True,
        max_length=100,
        required=True
    )
    email = CharField(required=False)
    senha = CharField(
        required=False,
        validators=[MinLengthValidator(8)],
        style={'input_type': 'password'}
    )
    id_endereco = PrimaryKeyRelatedField(
        queryset=Enderecos.objects.all(),
        write_only=True,
        required=False,
        allow_null=True
    )
    cpf = CharField(required=False)
    data_nascimento = DateField()
    sexo = CharField(max_length=1)

    class Meta:
        model = Clientes
        fields = [
            'nome',
            'usuario'
            'email',
            'senha',
            'id_endereco',
            'cpf',
            'data_nascimento',
            'sexo',
        ]

    def validate_cpf(self, value):
        if value:
            return self.validar_cpf(value)
        return value

    def update(self, instance, validated_data):
        # Atualiza dados do usuário
        usuario = instance.id_usuarios
        if 'nome' in validated_data:
            usuario.nome = validated_data['nome']
        if 'usuario' in validated_data:
            usuario.usuario = validated_data['usuario']
        if 'email' in validated_data:
            usuario.email = validated_data['email']
        if 'senha' in validated_data:
            usuario.senha = validated_data['senha']
        if 'id_endereco' in validated_data:
            usuario.id_endereco = validated_data['id_endereco']
        usuario.save()

        # Atualiza dados do cliente
        if 'cpf' in validated_data:
            instance.cpf = validated_data['cpf']
        if 'data_nascimento' in validated_data:
            instance.data_nascimento = validated_data['data_nascimento']
        if 'sexo' in validated_data:
            instance.sexo = validated_data['sexo']
        instance.save()

        return instance


class ParceiroComUsuarioCreateSerializer(ValidacaoCNPJMixin, ModelSerializer):
    nome = CharField(write_only=True, max_length=100)
    usuario = CharField(
        write_only=True,
        max_length=100,
        required=True
    )
    email = CharField(
        write_only=True,
        max_length=100,
        required=False,
        allow_null=True
    )
    senha = CharField(
        write_only=True,
        required=True,
        validators=[MinLengthValidator(8)],
        style={'input_type': 'password'}
    )
    id_endereco = PrimaryKeyRelatedField(
        queryset=Enderecos.objects.all(),
        write_only=True,
        required=False,
        allow_null=True
    )
    id_usuarios = PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Parceiros
        fields = [
            'id',             # Campo do parceiro
            'id_usuarios',    # Campo do usuário
            'usuario',        # Campo do usuário
            'cnpj',           # Campo do parceiro
            'criado_em',      # Campo do parceiro / usuário
            'atualizado_em',  # Campo do parceiro / usuário
            'nome',           # Campo do usuário
            'email',          # Campo do usuário
            'senha',          # Campo do usuário
            'id_endereco'     # Campo do usuário
        ]
        read_only_fields = [
            'id',
            'id_usuarios',
            'criado_em',
            'atualizado_em'
        ]

    def validate_cnpj(self, value):
        if value:
            return self.validar_cnpj(value)
        return value

    def create(self, validated_data):
        # Extrai os dados do usuário
        usuario_data = {
            'nome': validated_data.pop('nome'),
            'usuario': validated_data.pop('usuario'),
            'email': validated_data.pop('email', None),
            'senha': validated_data.pop('senha'),
            'id_endereco': validated_data.pop('id_endereco', None)
        }

        # Cria o usuário primeiro
        usuario = Usuarios.objects.create(**usuario_data)

        # Cria o parceiro vinculado ao usuário
        parceiro = Parceiros.objects.create(
            id_usuarios=usuario,
            **validated_data
        )

        return parceiro

    def update(self, instance, validated_data):
        # Remove campos do usuário que não devem ser atualizados aqui
        validated_data.pop('nome', None)
        validated_data.pop('usuario', None)
        validated_data.pop('email', None)
        validated_data.pop('senha', None)
        validated_data.pop('id_endereco', None)

        return super().update(instance, validated_data)


class ParceiroComUsuarioUpdateSerializer(ValidacaoCNPJMixin, ModelSerializer):
    nome = CharField(required=False)
    usuario = CharField(
        write_only=True,
        max_length=100,
        required=True
    )
    email = CharField(required=False)
    senha = CharField(
        required=False,
        validators=[MinLengthValidator(8)],
        style={'input_type': 'password'}
    )
    id_endereco = PrimaryKeyRelatedField(
        queryset=Enderecos.objects.all(),
        write_only=True,
        required=False,
        allow_null=True
    )
    cnpj = CharField(required=False)

    class Meta:
        model = Clientes
        fields = [
            'nome',
            'usuario',
            'email',
            'senha',
            'id_endereco',
            'cnpj'
        ]

    def validate_cnpj(self, value):
        if value:
            return self.validar_cnpj(value)
        return value

    def update(self, instance, validated_data):
        # Atualiza dados do usuário
        usuario = instance.id_usuarios
        if 'nome' in validated_data:
            usuario.nome = validated_data['nome']
        if 'usuario' in validated_data:
            usuario.usuario = validated_data['usuario']
        if 'email' in validated_data:
            usuario.email = validated_data['email']
        if 'senha' in validated_data:
            usuario.senha = validated_data['senha']
        if 'id_endereco' in validated_data:
            usuario.id_endereco = validated_data['id_endereco']
        usuario.save()

        # Atualiza dados do cliente
        if 'cnpj' in validated_data:
            instance.cnpj = validated_data['cnpj']
        instance.save()

        return instance


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


class ColetasSerializer(ModelSerializer):
    class Meta:
        model = Coletas
        fields = [
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
        fields = [
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
        fields = [
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
        fields = [
            'id_materiais',
            'id_parceiros',
        ]


class MateriaisPontosColetaSerializer(ModelSerializer):
    class Meta:
        model = MateriaisPontosColeta
        fields = [
            'id_materiais',
            'id_pontos_coleta',
        ]


class PagamentosSerializer(ModelSerializer):
    class Meta:
        model = Pagamentos
        fields = [
            'id',
            'valor_pagamento',
            'saldo_pagamento',
            'estado_pagamento',
            'criado_em',
            'atualizado_em',
        ]


class PontosColetaSerializer(ModelSerializer):
    class Meta:
        model = PontosColeta
        fields = [
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
        fields = [
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
        fields = [
            'id_usuarios',
            'numero',
            'criado_em',
            'atualizado_em',
        ]
