from rest_framework import serializers
from .models import Clientes, Documentos, DocumentosImpostos, DocumentosProdutos, Impostos, Pessoas, Produtos

class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = '__all__'

class DocumentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documentos
        fields = '__all__'

class DocumentosImpostosSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentosImpostos
        fields = '__all__'

class DocumentosProdutosSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentosProdutos
        fields = '__all__'

class ImpostosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Impostos
        fields = '__all__'

class PessoasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoas
        fields = '__all__'

class ProdutosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtos
        fields = '__all__'
