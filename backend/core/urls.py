from django.urls import path
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
    path('v1/avaliacoes/', AvaliacoesApiView.as_view(), name='avaliacoes-list'),
    path('v1/avaliacoes/<int:id>/', AvaliacoesApiViewDetail.as_view(), name='avaliacoes-detail'),

    path('v1/clientes/', ClientesApiView.as_view(), name='clientes-list'),
    path('v1/clientes/<int:id>/', ClientesApiViewDetail.as_view(), name='clientes-detail'),

    path('v1/coletas/', ColetasApiView.as_view(), name='coletas-list'),
    path('v1/coletas/<int:id>/', ColetasApiViewDetail.as_view(), name='coletas-detail'),

    path('v1/enderecos/', EnderecosApiView.as_view(), name='enderecos-list'),
    path('v1/enderecos/<int:id>/', EnderecosApiViewDetail.as_view(), name='enderecos-detail'),

    path('v1/materiais/', MateriaisApiView.as_view(), name='materiais-list'),
    path('v1/materiais/<int:id>/', MateriaisApiViewDetail.as_view(), name='materiais-detail'),

    path('v1/materiais-parceiros/', MateriaisParceirosApiView.as_view(), name='materiais-parceiros-list'),
    path('v1/materiais-parceiros/<int:id>/', MateriaisParceirosApiViewDetail.as_view(), name='materiais-parceiros-detail'),

    path('v1/materiais-pontos-coleta/', MateriaisPontosColetaApiView.as_view(), name='materiais-pontos-coleta-list'),
    path('v1/materiais-pontos-coleta/<int:id>/', MateriaisPontosColetaApiViewDetail.as_view(), name='materiais-pontos-coleta-detail'),

    path('v1/pagamentos/', PagamentosApiView.as_view(), name='pagamentos-list'),
    path('v1/pagamentos/<int:id>/', PagamentosApiViewDetail.as_view(), name='pagamentos-detail'),

    path('v1/parceiros/', ParceirosApiView.as_view(), name='parceiros-list'),
    path('v1/parceiros/<int:id>/', ParceirosApiViewDetail.as_view(), name='parceiros-detail'),

    path('v1/pontos-coleta/', PontosColetaApiView.as_view(), name='pontos-coleta-list'),
    path('v1/pontos-coleta/<int:id>/', PontosColetaApiViewDetail.as_view(), name='pontos-coleta-detail'),

    path('v1/solicitacoes/', SolicitacoesApiView.as_view(), name='solicitacoes-list'),
    path('v1/solicitacoes/<int:id>/', SolicitacoesApiViewDetail.as_view(), name='solicitacoes-detail'),

    path('v1/telefones/', TelefonesApiView.as_view(), name='telefones-list'),
    path('v1/telefones/<int:id>/', TelefonesApiViewDetail.as_view(), name='telefones-detail'),

    path('v1/usuarios/', UsuariosApiView.as_view(), name='usuarios-list'),
    path('v1/usuarios/<int:id>/', UsuariosApiViewDetail.as_view(), name='usuarios-detail'),
]
