from django.db import models

# Criado classe Base para que os campos que são iguais em outras
# tabelas sejam replicadas de uma forma mais inteligente,
# sem repetição de códigos


class Base(models.Model):
    criado_em = models.DateTimeField()
    atualizado_em = models.DateTimeField()

    class Meta:
        abstract = True


class Avaliacoes(Base):
    id = models.SmallAutoField(primary_key=True)
    id_parceiros = models.ForeignKey(
        'Parceiros', models.DO_NOTHING, db_column='id_parceiros')
    id_clientes = models.ForeignKey(
        'Clientes', models.DO_NOTHING, db_column='id_clientes')
    nota_parceiros = models.SmallIntegerField()
    descricao_parceiros = models.CharField(
        max_length=300, blank=True, null=True)
    nota_clientes = models.SmallIntegerField()
    descricao_clientes = models.CharField(
        max_length=300, blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = 'avaliacoes'


class Clientes(Base):
    id = models.SmallAutoField(primary_key=True)
    id_usuarios = models.OneToOneField(
        'Usuarios', models.DO_NOTHING, db_column='id_usuarios')
    cpf = models.CharField(unique=True, max_length=15)

    class Meta:
        managed = False
        db_table = 'clientes'


class Coletas(Base):
    id = models.SmallAutoField(primary_key=True)
    id_clientes = models.ForeignKey(
        Clientes, models.DO_NOTHING, db_column='id_clientes')
    id_parceiros = models.ForeignKey(
        'Parceiros', models.DO_NOTHING, db_column='id_parceiros',
        blank=True, null=True)
    id_materiais = models.ForeignKey(
        'Materiais', models.DO_NOTHING, db_column='id_materiais')
    peso_material = models.DecimalField(
        max_digits=15, decimal_places=4, blank=True, null=True)
    quantidade_material = models.SmallIntegerField(blank=True, null=True)
    id_enderecos = models.ForeignKey(
        'Enderecos', models.DO_NOTHING, db_column='id_enderecos')
    id_solicitacoes = models.ForeignKey(
        'Solicitacoes', models.DO_NOTHING, db_column='id_solicitacoes')
    id_pagamentos = models.ForeignKey(
        'Pagamentos', models.DO_NOTHING, db_column='id_pagamentos')

    class Meta:
        managed = False
        db_table = 'coletas'


class Enderecos(Base):
    id = models.SmallAutoField(primary_key=True)
    cep = models.CharField(max_length=15)
    estado = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    rua = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'enderecos'


class Materiais(Base):
    id = models.SmallAutoField(primary_key=True)
    nome = models.CharField(unique=True, max_length=50)
    descricao = models.CharField(max_length=150, blank=True, null=True)
    preco = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'materiais'


class MateriaisParceiros(models.Model):
    # The composite primary key (id_materiais, id_parceiros)
    # found, that is not supported. The first column is selected.
    id_materiais = models.OneToOneField(
        Materiais, models.DO_NOTHING, db_column='id_materiais',
        primary_key=True)
    id_parceiros = models.ForeignKey(
        'Parceiros', models.DO_NOTHING, db_column='id_parceiros')

    class Meta:
        managed = False
        db_table = 'materiais_parceiros'
        unique_together = (('id_materiais', 'id_parceiros'),)


class MateriaisPontosColeta(models.Model):
    # The composite primary key (id_materiais, id_pontos_coleta)
    # found, that is not supported. The first column is selected.
    id_materiais = models.OneToOneField(
        Materiais, models.DO_NOTHING, db_column='id_materiais',
        primary_key=True)
    id_pontos_coleta = models.ForeignKey(
        'PontosColeta', models.DO_NOTHING, db_column='id_pontos_coleta')

    class Meta:
        managed = False
        db_table = 'materiais_pontos_coleta'
        unique_together = (('id_materiais', 'id_pontos_coleta'),)


class Pagamentos(Base):
    id = models.SmallAutoField(primary_key=True)
    valor_pagamento = models.TextField()  # This field type is a guess.
    saldo_pagamento = models.TextField()  # This field type is a guess.
    estado_pagamento = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'pagamentos'


class Parceiros(Base):
    id = models.SmallAutoField(primary_key=True)
    id_usuarios = models.OneToOneField(
        'Usuarios', models.DO_NOTHING, db_column='id_usuarios')
    cnpj = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'parceiros'


class PontosColeta(Base):
    id = models.SmallAutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    id_enderecos = models.ForeignKey(
        Enderecos, models.DO_NOTHING, db_column='id_enderecos')
    descricao = models.CharField(max_length=200, blank=True, null=True)
    horario_funcionamento = models.CharField(
        max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pontos_coleta'


class Solicitacoes(Base):
    id = models.SmallAutoField(primary_key=True)
    estado_solicitacao = models.CharField(max_length=10)
    observacoes = models.CharField(max_length=100, blank=True, null=True)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    finalizado_em = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'solicitacoes'


class Telefones(Base):
    id_usuarios = models.OneToOneField(
        'Usuarios', models.DO_NOTHING,
        db_column='id_usuarios', primary_key=True)
    numero = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'telefones'


class Usuarios(Base):
    id = models.SmallAutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100, blank=True, null=True)
    senha = models.TextField()
    id_endereco = models.ForeignKey(
        Enderecos, models.DO_NOTHING, db_column='id_endereco',
        blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuarios'
