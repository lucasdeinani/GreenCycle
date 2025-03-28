from django.urls import path, include
<<<<<<< Updated upstream
from django.contrib import admin
from .views import (
    AvaliacoesApiView, AvaliacoesApiViewDetail, ClientesApiView,
    ClientesApiViewDetail, ColetasApiView, ColetasApiViewDetail,
    EnderecosApiView, EnderecosApiViewDetail, MateriaisApiView,
    MateriaisApiViewDetail, MateriaisParceirosApiView,
    MateriaisParceirosApiViewDetail, MateriaisPontosColetaApiView,
    MateriaisPontosColetaApiViewDetail, PagamentosApiView,
    PagamentosApiViewDetail, ParceirosApiView, ParceirosApiViewDetail,
    PontosColetaApiView, PontosColetaApiViewDetail, SolicitacoesApiView,
    SolicitacoesApiViewDetail, TelefonesApiView, TelefonesApiViewDetail,
    UsuariosApiView, UsuariosApiViewDetail
)

urlpatterns = [
    path('v1/api', AvaliacoesApiView.as_view()),
    path('v1/api/<int:id>', AvaliacoesApiViewDetail.as_view()),
    path('v1/api', ClientesApiView.as_view()),
    path('v1/api/<int:id>', ClientesApiViewDetail.as_view()),
    path('v1/api', ColetasApiView.as_view()),
    path('v1/api/<int:id>', ColetasApiViewDetail.as_view()),
    path('v1/api', EnderecosApiView.as_view()),
    path('v1/api/<int:id>', EnderecosApiViewDetail.as_view()),
    path('v1/api', MateriaisApiView.as_view()),
    path('v1/api/<int:id>', MateriaisApiViewDetail.as_view()),
    path('v1/api', MateriaisParceirosApiView.as_view()),
    path('v1/api/<int:id>', MateriaisParceirosApiViewDetail.as_view()),
    path('v1/api', MateriaisPontosColetaApiView.as_view()),
    path('v1/api/<int:id>', MateriaisPontosColetaApiViewDetail.as_view()),
    path('v1/api', PagamentosApiView.as_view()),
    path('v1/api/<int:id>', PagamentosApiViewDetail.as_view()),
    path('v1/api', ParceirosApiView.as_view()),
    path('v1/api/<int:id>', ParceirosApiViewDetail.as_view()),
    path('v1/api', PontosColetaApiView.as_view()),
    path('v1/api/<int:id>', PontosColetaApiViewDetail.as_view()),
    path('v1/api', SolicitacoesApiView.as_view()),
    path('v1/api/<int:id>', SolicitacoesApiViewDetail.as_view()),
    path('v1/api', TelefonesApiView.as_view()),
    path('v1/api/<int:id>', TelefonesApiViewDetail.as_view()),
    path('v1/api', UsuariosApiView.as_view()),
    path('v1/api/<int:id>', UsuariosApiViewDetail.as_view()),
=======
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# from . import admin
from .views import (
    UsuariosCreateViewSet, ClientesCreateViewSet, ParceirosCreateViewSet,
    AvaliacoesViewSet, ColetasViewSet, EnderecosViewSet, MateriaisViewSet,
    MateriaisParceirosViewSet, MateriaisPontosColetaViewSet,
    PagamentosViewSet, PontosColetaViewSet, SolicitacoesViewSet,
    TelefonesViewSet, home
)

# Configuração do router para as viewsets da API
router = DefaultRouter()

# Rotas para cadastro e gerenciamento de usuários
router.register(r'usuarios', UsuariosCreateViewSet, basename='usuarios')
router.register(r'clientes', ClientesCreateViewSet, basename='clientes')
router.register(r'parceiros', ParceirosCreateViewSet, basename='parceiros')

# Rotas para entidades principais
router.register(r'avaliacoes', AvaliacoesViewSet, basename='avaliacoes')
router.register(r'coletas', ColetasViewSet, basename='coletas')
router.register(r'enderecos', EnderecosViewSet, basename='enderecos')
router.register(r'materiais', MateriaisViewSet, basename='materiais')

# Rotas para relacionamentos muitos-para-muitos
router.register(r'materiais-parceiros', MateriaisParceirosViewSet,
                basename='materiais-parceiros')
router.register(r'materiais-pontos-coleta', MateriaisPontosColetaViewSet,
                basename='materiais-pontos-coleta')

# Rotas para transações e operações
router.register(r'pagamentos', PagamentosViewSet, basename='pagamentos')
router.register(
    r'pontos-coleta',
    PontosColetaViewSet,
    basename='pontos-coleta'
)
router.register(r'solicitacoes', SolicitacoesViewSet, basename='solicitacoes')
router.register(r'telefones', TelefonesViewSet, basename='telefones')

urlpatterns = [
    # Rota inicial da API
    path('', home, name='home'),

    # Painel de administração
    path('admin/', django_admin.site.urls),

    # API v1 - Todas as rotas registradas no router
    path('v1/', include(router.urls)),

    # Autenticação JWT
    path('v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(
        'v1/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
>>>>>>> Stashed changes
]
