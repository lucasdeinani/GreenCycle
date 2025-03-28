from rest_framework.serializers import (
    ModelSerializer, ValidationError, CharField
)
from .models import (
    Avaliacoes, Clientes, Coletas, Enderecos,
    Materiais, MateriaisParceiros, MateriaisPontosColeta, Pagamentos,
    Parceiros, PontosColeta, Solicitacoes, Telefones, Usuarios
)
from django.core.validators import MinLengthValidator
# from django.contrib.auth.hashers import make_password
import re


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


class ClienteCreateSerializer(ModelSerializer):
    usuario = UsuarioCreateSerializer(source='id_usuarios')

    class Meta:
        model = Clientes
        fields = [
            'id',
            'usuario',
            'cpf',
            'criado_em',
            'atualizado_em',
        ]

    def validate_cpf(self, value):
        # Remove caracteres não numéricos
        cpf = re.sub(r'[^0-9]', '', value)

        # Verifica se tem 11 dígitos
        if len(cpf) != 11:
            raise ValidationError('CPF deve conter 11 dígitos')

        # Verifica se todos os dígitos são iguais
        if cpf == cpf[0] * 11:
            raise ValidationError('CPF inválido')

        # Validação dos dígitos verificadores
        for i in range(9, 11):
            value = sum(int(cpf[num]) * ((i+1) - num) for num in range(0, i))
            digit = ((value * 10) % 11) % 10
            if digit != int(cpf[i]):
                raise ValidationError('CPF inválido')

        # Retorna no formato 000.000.000-00
        return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'

    def create(self, validated_data):
        usuario_data = validated_data.pop('usuario')
        usuario_serializer = UsuarioCreateSerializer(data=usuario_data)

        if usuario_serializer.is_valid():
            usuario = usuario_serializer.save()
            cliente = Clientes.objects.create(
                id_usuarios=usuario, **validated_data
            )
            return cliente
        raise ValidationError(usuario_serializer.errors)


class ParceiroCreateSerializer(ModelSerializer):
    usuario = UsuarioCreateSerializer(source='id_usuarios')

    class Meta:
        model = Parceiros
        fields = [
            'id',
            'usuario',
            'cnpj',
            'criado_em',
            'atualizado_em',
        ]

    def validate_cnpj(self, value):
        # Remove caracteres não numéricos
        cnpj = re.sub(r'[^0-9]', '', value)

        # Verifica se tem 14 dígitos
        if len(cnpj) != 14:
            raise ValidationError('CNPJ deve conter 14 dígitos')

        # Verifica se todos os dígitos são iguais
        if cnpj == cnpj[0] * 14:
            raise ValidationError('CNPJ inválido')

        # Validação do primeiro dígito verificador
        peso = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        soma = sum(int(cnpj[i]) * peso[i] for i in range(12))
        resto = soma % 11
        digito1 = 0 if resto < 2 else 11 - resto

        # Validação do segundo dígito verificador
        peso = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        soma = sum(int(cnpj[i]) * peso[i] for i in range(13))
        resto = soma % 11
        digito2 = 0 if resto < 2 else 11 - resto

        # Verifica os dígitos
        if int(cnpj[12]) != digito1 or int(cnpj[13]) != digito2:
            raise ValidationError('CNPJ inválido')

        # Retorna no formato 00.000.000/0000-00
        return f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}'

    def create(self, validated_data):
        usuario_data = validated_data.pop('usuario')
        usuario_serializer = UsuarioCreateSerializer(data=usuario_data)

        if usuario_serializer.is_valid():
            usuario = usuario_serializer.save()
            parceiro = Parceiros.objects.create(
                id_usuarios=usuario, **validated_data
            )
            return parceiro
        raise ValidationError(usuario_serializer.errors)


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
