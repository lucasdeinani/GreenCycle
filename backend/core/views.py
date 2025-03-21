from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from .models import (
    Avaliacoes, Clientes, Coletas, Enderecos,
    Materiais, MateriaisParceiros, MateriaisPontosColeta, Pagamentos,
    Parceiros, PontosColeta, Solicitacoes, Telefones, Usuarios
)
from .serializers import (
    AvaliacoesSerializer, ClientesSerializer, ColetasSerializer,
    EnderecosSerializer, MateriaisSerializer, MateriaisParceirosSerializer,
    MateriaisPontosColetaSerializer, PagamentosSerializer, ParceirosSerializer,
    PontosColetaSerializer, SolicitacoesSerializer, TelefonesSerializer,
    UsuariosSerializer
)

def home(request):
    return JsonResponse({"mensagem": "Bem-vindo à API do GreenCycle!"})

class AvaliacoesApiView(APIView):
    def get(self, request):
        avaliacoes = Avaliacoes.objects.all()
        serializer = AvaliacoesSerializer(avaliacoes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AvaliacoesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class AvaliacoesApiViewDetail(APIView):
    def get_object(self, pk):
        try:
            return Avaliacoes.objects.get(pk=pk)
        except Avaliacoes.DoesNotExist:
            return None

    def get(self, request, id):
        avaliacao = self.get_object(id)
        serializer = AvaliacoesSerializer(avaliacao)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def put(self, request, id):
        avaliacao = self.get_object(id)
        if (avaliacao == None):
            return Response(
                status=status.HTTP_200_OK, data={
                    'error': 'Not found data'
                }
            )
        serializer = AvaliacoesSerializer(avaliacao, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        avaliacao = self.get_object(id)
        avaliacao.delete()
        response = {'deleted': True}
        return Response(status=status.HTTP_204_NO_CONTENT, data=response)


class ClientesApiView(APIView):
    def get(self, request):
        clientes = Clientes.objects.all()
        serializer = ClientesSerializer(clientes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClientesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class ClientesApiViewDetail(APIView):
    def get_object(self, pk):
        try:
            return Clientes.objects.get(pk=pk)
        except Clientes.DoesNotExist:
            return None

    def get(self, request, id):
        cliente = self.get_object(id)
        serializer = ClientesSerializer(cliente)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def put(self, request, id):
        cliente = self.get_object(id)
        if (cliente == None):
            return Response(
                status=status.HTTP_200_OK, data={
                    'error': 'Not found data'
                }
            )
        serializer = ClientesSerializer(cliente, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        cliente = self.get_object(id)
        cliente.delete()
        response = {'deleted': True}
        return Response(status=status.HTTP_204_NO_CONTENT, data=response)


class ColetasApiView(APIView):
    def get(self, request):
        coletas = Coletas.objects.all()
        serializer = ColetasSerializer(coletas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ColetasSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class ColetasApiViewDetail(APIView):
    def get_object(self, pk):
        try:
            return Coletas.objects.get(pk=pk)
        except Coletas.DoesNotExist:
            return None

    def get(self, request, id):
        coleta = self.get_object(id)
        serializer = ColetasSerializer(coleta)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def put(self, request, id):
        coleta = self.get_object(id)
        if (coleta == None):
            return Response(
                status=status.HTTP_200_OK, data={
                    'error': 'Not found data'
                }
            )
        serializer = ColetasSerializer(coleta, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        coleta = self.get_object(id)
        coleta.delete()
        response = {'deleted': True}
        return Response(status=status.HTTP_204_NO_CONTENT, data=response)


class EnderecosApiView(APIView):
    def get(self, request):
        enderecos = Enderecos.objects.all()
        serializer = EnderecosSerializer(enderecos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EnderecosSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class EnderecosApiViewDetail(APIView):
    def get_object(self, pk):
        try:
            return Enderecos.objects.get(pk=pk)
        except Enderecos.DoesNotExist:
            return None

    def get(self, request, id):
        endereco = self.get_object(id)
        serializer = EnderecosSerializer(endereco)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def put(self, request, id):
        endereco = self.get_object(id)
        if (endereco == None):
            return Response(
                status=status.HTTP_200_OK, data={
                    'error': 'Not found data'
                }
            )
        serializer = EnderecosSerializer(endereco, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        endereco = self.get_object(id)
        endereco.delete()
        response = {'deleted': True}
        return Response(status=status.HTTP_204_NO_CONTENT, data=response)


class MateriaisApiView(APIView):
    def get(self, request):
        materiais = Materiais.objects.all()
        serializer = MateriaisSerializer(materiais, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MateriaisSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class MateriaisApiViewDetail(APIView):
    def get_object(self, pk):
        try:
            return Materiais.objects.get(pk=pk)
        except Materiais.DoesNotExist:
            return None

    def get(self, request, id):
        material = self.get_object(id)
        serializer = MateriaisSerializer(material)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def put(self, request, id):
        material = self.get_object(id)
        if (material == None):
            return Response(
                status=status.HTTP_200_OK, data={
                    'error': 'Not found data'
                }
            )
        serializer = MateriaisSerializer(material, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        material = self.get_object(id)
        material.delete()
        response = {'deleted': True}
        return Response(status=status.HTTP_204_NO_CONTENT, data=response)


class MateriaisParceirosApiView(APIView):
    def get(self, request):
        materiasParceiros = MateriaisParceiros.objects.all()
        serializer = MateriaisParceirosSerializer(materiasParceiros, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MateriaisParceirosSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class MateriaisParceirosApiViewDetail(APIView):
    def get_object(self, pk):
        try:
            return MateriaisParceiros.objects.get(pk=pk)
        except MateriaisParceiros.DoesNotExist:
            return None

    def get(self, request, id):
        materialParceiro = self.get_object(id)
        serializer = MateriaisParceirosSerializer(materialParceiro)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def put(self, request, id):
        materialParceiro = self.get_object(id)
        if (materialParceiro == None):
            return Response(
                status=status.HTTP_200_OK, data={
                    'error': 'Not found data'
                }
            )
        serializer = MateriaisParceirosSerializer(
            materialParceiro, data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        materialParceiro = self.get_object(id)
        materialParceiro.delete()
        response = {'deleted': True}
        return Response(status=status.HTTP_204_NO_CONTENT, data=response)


class MateriaisPontosColetaApiView(APIView):
    def get(self, request):
        materiaisPontosColeta = MateriaisPontosColeta.objects.all()
        serializer = MateriaisPontosColetaSerializer(
            materiaisPontosColeta, many=True
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = MateriaisPontosColetaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class MateriaisPontosColetaApiViewDetail(APIView):
    def get_object(self, pk):
        try:
            return MateriaisPontosColeta.objects.get(pk=pk)
        except MateriaisPontosColeta.DoesNotExist:
            return None

    def get(self, request, id):
        materialPontoColeta = self.get_object(id)
        serializer = MateriaisPontosColetaSerializer(materialPontoColeta)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def put(self, request, id):
        materialPontoColeta = self.get_object(id)
        if (materialPontoColeta == None):
            return Response(
                status=status.HTTP_200_OK, data={
                    'error': 'Not found data'
                }
            )
        serializer = MateriaisPontosColetaSerializer(
            materialPontoColeta, data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        materialPontoColeta = self.get_object(id)
        materialPontoColeta.delete()
        response = {'deleted': True}
        return Response(status=status.HTTP_204_NO_CONTENT, data=response)


class PagamentosApiView(APIView):
    def get(self, request):
        pagamentos = Pagamentos.objects.all()
        serializer = PagamentosSerializer(pagamentos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PagamentosSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class PagamentosApiViewDetail(APIView):
    def get_object(self, pk):
        try:
            return Pagamentos.objects.get(pk=pk)
        except Pagamentos.DoesNotExist:
            return None

    def get(self, request, id):
        pagamento = self.get_object(id)
        serializer = PagamentosSerializer(pagamento)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def put(self, request, id):
        pagamento = self.get_object(id)
        if (pagamento == None):
            return Response(
                status=status.HTTP_200_OK, data={
                    'error': 'Not found data'
                }
            )
        serializer = PagamentosSerializer(pagamento, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        pagamento = self.get_object(id)
        pagamento.delete()
        response = {'deleted': True}
        return Response(status=status.HTTP_204_NO_CONTENT, data=response)


class ParceirosApiView(APIView):
    def get(self, request):
        parceiros = Parceiros.objects.all()
        serializer = ParceirosSerializer(parceiros, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ParceirosSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class ParceirosApiViewDetail(APIView):
    def get_object(self, pk):
        try:
            return Parceiros.objects.get(pk=pk)
        except Parceiros.DoesNotExist:
            return None

    def get(self, request, id):
        parceiro = self.get_object(id)
        serializer = ParceirosSerializer(parceiro)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def put(self, request, id):
        parceiro = self.get_object(id)
        if (parceiro == None):
            return Response(
                status=status.HTTP_200_OK, data={
                    'error': 'Not found data'
                }
            )
        serializer = ParceirosSerializer(parceiro, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        parceiro = self.get_object(id)
        parceiro.delete()
        response = {'deleted': True}
        return Response(status=status.HTTP_204_NO_CONTENT, data=response)


class PontosColetaApiView(APIView):
    def get(self, request):
        pontosColeta = PontosColeta.objects.all()
        serializer = PontosColetaSerializer(pontosColeta, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PontosColetaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class PontosColetaApiViewDetail(APIView):
    def get_object(self, pk):
        try:
            return PontosColeta.objects.get(pk=pk)
        except PontosColeta.DoesNotExist:
            return None

    def get(self, request, id):
        pontoColeta = self.get_object(id)
        serializer = PontosColetaSerializer(pontoColeta)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def put(self, request, id):
        pontoColeta = self.get_object(id)
        if (pontoColeta == None):
            return Response(
                status=status.HTTP_200_OK, data={
                    'error': 'Not found data'
                }
            )
        serializer = PontosColetaSerializer(pontoColeta, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        pontoColeta = self.get_object(id)
        pontoColeta.delete()
        response = {'deleted': True}
        return Response(status=status.HTTP_204_NO_CONTENT, data=response)


class SolicitacoesApiView(APIView):
    def get(self, request):
        solicitacoes = Solicitacoes.objects.all()
        serializer = SolicitacoesSerializer(solicitacoes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SolicitacoesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class SolicitacoesApiViewDetail(APIView):
    def get_object(self, pk):
        try:
            return Solicitacoes.objects.get(pk=pk)
        except Solicitacoes.DoesNotExist:
            return None

    def get(self, request, id):
        solicitacao = self.get_object(id)
        serializer = SolicitacoesSerializer(solicitacao)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def put(self, request, id):
        solicitacao = self.get_object(id)
        if (solicitacao == None):
            return Response(
                status=status.HTTP_200_OK, data={
                    'error': 'Not found data'
                }
            )
        serializer = SolicitacoesSerializer(solicitacao, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        solicitacao = self.get_object(id)
        solicitacao.delete()
        response = {'deleted': True}
        return Response(status=status.HTTP_204_NO_CONTENT, data=response)


class TelefonesApiView(APIView):
    def get(self, request):
        telefones = Telefones.objects.all()
        serializer = TelefonesSerializer(telefones, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TelefonesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class TelefonesApiViewDetail(APIView):
    def get_object(self, pk):
        try:
            return Telefones.objects.get(pk=pk)
        except Telefones.DoesNotExist:
            return None

    def get(self, request, id):
        telefone = self.get_object(id)
        serializer = TelefonesSerializer(telefone)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def put(self, request, id):
        telefone = self.get_object(id)
        if (telefone == None):
            return Response(
                status=status.HTTP_200_OK, data={
                    'error': 'Not found data'
                }
            )
        serializer = TelefonesSerializer(telefone, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        telefone = self.get_object(id)
        telefone.delete()
        response = {'deleted': True}
        return Response(status=status.HTTP_204_NO_CONTENT, data=response)


class UsuariosApiView(APIView):
    def get(self, request):
        usuarios = Usuarios.objects.all()
        serializer = UsuariosSerializer(usuarios, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UsuariosSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class UsuariosApiViewDetail(APIView):
    def get_object(self, pk):
        try:
            return Usuarios.objects.get(pk=pk)
        except Usuarios.DoesNotExist:
            return None

    def get(self, request, id):
        usuario = self.get_object(id)
        serializer = UsuariosSerializer(usuario)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def put(self, request, id):
        usuario = self.get_object(id)
        if (usuario == None):
            return Response(
                status=status.HTTP_200_OK, data={
                    'error': 'Not found data'
                }
            )
        serializer = UsuariosSerializer(usuario, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        usuario = self.get_object(id)
        usuario.delete()
        response = {'deleted': True}
        return Response(status=status.HTTP_204_NO_CONTENT, data=response)
