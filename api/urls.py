from django.urls import path, include
from rest_framework import routers
from .views import (
    index,
    ClientesViewSet,
    DocumentosViewSet,
    DocumentosImpostosViewSet,
    DocumentosProdutosViewSet,
    ImpostosViewSet,
    PessoasViewSet,
    ProdutosViewSet
)

# Configurando as rotas da API REST
router = routers.DefaultRouter()
router.register(r'clientes', ClientesViewSet)
router.register(r'documentos', DocumentosViewSet)
router.register(r'documentos-impostos', DocumentosImpostosViewSet)
router.register(r'documentos-produtos', DocumentosProdutosViewSet)
router.register(r'impostos', ImpostosViewSet)
router.register(r'pessoas', PessoasViewSet)
router.register(r'produtos', ProdutosViewSet)

urlpatterns = [
    path('', index, name='index'),   # Página de boas-vindas
    path('api/', include(router.urls)),  # API REST
]
