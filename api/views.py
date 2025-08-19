from django.shortcuts import render
from rest_framework import viewsets
from .models import Clientes, Documentos, DocumentosImpostos, DocumentosProdutos, Impostos, Pessoas, Produtos
from .serializers import (
    ClientesSerializer,
    DocumentosSerializer,
    DocumentosImpostosSerializer,
    DocumentosProdutosSerializer,
    ImpostosSerializer,
    PessoasSerializer,
    ProdutosSerializer
)

# View da página de boas-vindas
def index(request):
    return render(request, "index.html")  # index.html dentro de api/templates/

# ViewSets da API
class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer

class DocumentosViewSet(viewsets.ModelViewSet):
    queryset = Documentos.objects.all()
    serializer_class = DocumentosSerializer

class DocumentosImpostosViewSet(viewsets.ModelViewSet):
    queryset = DocumentosImpostos.objects.all()
    serializer_class = DocumentosImpostosSerializer

class DocumentosProdutosViewSet(viewsets.ModelViewSet):
    queryset = DocumentosProdutos.objects.all()
    serializer_class = DocumentosProdutosSerializer

class ImpostosViewSet(viewsets.ModelViewSet):
    queryset = Impostos.objects.all()
    serializer_class = ImpostosSerializer

class PessoasViewSet(viewsets.ModelViewSet):
    queryset = Pessoas.objects.all()
    serializer_class = PessoasSerializer

class ProdutosViewSet(viewsets.ModelViewSet):
    queryset = Produtos.objects.all()
    serializer_class = ProdutosSerializer
