# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class Clientes(models.Model):
    cliente_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    pais = models.CharField(max_length=50, blank=True, null=True)
    cnpj_cpf = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clientes'




class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Documentos(models.Model):
    documento_id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Clientes, models.DO_NOTHING, blank=True, null=True)
    tipo_documento = models.CharField(max_length=50, blank=True, null=True)
    data_emissao = models.DateField(blank=True, null=True)
    numero_documento = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documentos'


class DocumentosImpostos(models.Model):
    doc_imposto_id = models.AutoField(primary_key=True)
    documento = models.ForeignKey(Documentos, models.DO_NOTHING, blank=True, null=True)
    imposto = models.ForeignKey('Impostos', models.DO_NOTHING, blank=True, null=True)
    valor_base = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    aliquota = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    valor_imposto = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documentos_impostos'


class DocumentosProdutos(models.Model):
    doc_produto_id = models.AutoField(primary_key=True)
    documento = models.ForeignKey(Documentos, models.DO_NOTHING, blank=True, null=True)
    produto = models.ForeignKey('Produtos', models.DO_NOTHING, blank=True, null=True)
    quantidade = models.IntegerField(blank=True, null=True)
    valor_unitario = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documentos_produtos'


class Impostos(models.Model):
    imposto_id = models.AutoField(primary_key=True)
    nome_imposto = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'impostos'


class Pessoas(models.Model):
    nome = models.CharField(max_length=30)
    nascimento = models.DateField(blank=True, null=True)
    sexo = models.CharField(max_length=1, blank=True, null=True)
    peso = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    altura = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    nacionalidade = models.CharField(max_length=20, blank=True, null=True)
    profissao = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pessoas'


class Produtos(models.Model):
    produto_id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100, blank=True, null=True)
    ncm = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'produtos'
