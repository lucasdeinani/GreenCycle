from django.urls import path, include
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
]
