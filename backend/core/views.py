<<<<<<< Updated upstream
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
=======
from rest_framework import viewsets, status
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# from rest_framework.decorators import action
from django.core.cache import cache
from django.http import JsonResponse
>>>>>>> Stashed changes
from .models import (
    Avaliacoes, Clientes, Coletas, Enderecos,
    Materiais, MateriaisParceiros, MateriaisPontosColeta, Pagamentos,
    Parceiros, PontosColeta, Solicitacoes, Telefones, Usuarios
)
from .serializers import (
    UsuarioCreateSerializer, ClienteCreateSerializer, ParceiroCreateSerializer,
    AvaliacoesSerializer, ColetasSerializer, EnderecosSerializer,
    MateriaisSerializer, MateriaisParceirosSerializer,
    MateriaisPontosColetaSerializer, PagamentosSerializer,
    PontosColetaSerializer, SolicitacoesSerializer, TelefonesSerializer
)

<<<<<<< Updated upstream

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
=======

def home(request):
    return JsonResponse({"mensagem": "APIs GreenCycle App"})


# ViewSets
class UsuariosCreateViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuarioCreateSerializer

    def create(self, request, *args, **kwargs):
        # Verifica se o email já está cadastrado
        email = request.data.get('email')
        if email and Usuarios.objects.filter(email=email).exists():
            return Response(
                {'email': 'Já existe um usuário com este email.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer_class = self.get_serializer(data=request.data)
        serializer_class.is_valid(raise_exception=True)

        # Cria o usuário com a senha já validada pelo serializer_class
        self.perform_create(serializer_class)

        headers = self.get_success_headers(serializer_class.data)

        # Remove cache de listagem de usuários se existir
        cache.delete('usuarios_list')

        return Response(
            serializer_class.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )
    # permission_classes = [IsAuthenticated]


class ClientesCreateViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClienteCreateSerializer

    def create(self, request, *args, **kwargs):
        # Verifica se o email já está cadastrado
        email = request.data.get('usuario', {}).get('email')
        if email and Usuarios.objects.filter(email=email).exists():
            return Response(
                {'email': 'Já existe um usuário com este email.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Verifica se o CPF já está cadastrado
        cpf = request.data.get('cpf')
        if cpf and Clientes.objects.filter(cpf=cpf).exists():
            return Response(
                {'cpf': 'Já existe um cliente com este CPF.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer_class = self.get_serializer(data=request.data)
        serializer_class.is_valid(raise_exception=True)
        self.perform_create(serializer_class)
        headers = self.get_success_headers(serializer_class.data)

        # Remove cache de listagem de clientes se existir
        cache.delete('clientes_list')

        return Response(
            serializer_class.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )
    # permission_classes = [IsAuthenticated]


class ParceirosCreateViewSet(viewsets.ModelViewSet):
    queryset = Parceiros.objects.all()
    serializer_class = ParceiroCreateSerializer

    def create(self, request, *args, **kwargs):
        # Verifica se o email já está cadastrado
        email = request.data.get('usuario', {}).get('email')
        if email and Usuarios.objects.filter(email=email).exists():
            return Response(
                {'email': 'Já existe um usuário com este email.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Verifica se o CNPJ já está cadastrado
        cnpj = request.data.get('cnpj')
        if cnpj and Parceiros.objects.filter(cnpj=cnpj).exists():
            return Response(
                {'cnpj': 'Já existe um parceiro com este CNPJ.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer_class = self.get_serializer(data=request.data)
        serializer_class.is_valid(raise_exception=True)
        self.perform_create(serializer_class)
        headers = self.get_success_headers(serializer_class.data)

        # Remove cache de listagem de parceiros se existir
        cache.delete('parceiros_list')

        return Response(
            serializer_class.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )
    # permission_classes = [IsAuthenticated]


class AvaliacoesViewSet(viewsets.ModelViewSet):
    queryset = Avaliacoes.objects.all()
    serializer_class = AvaliacoesSerializer
    # permission_classes = [IsAuthenticated]


class ColetasViewSet(viewsets.ModelViewSet):
    queryset = Coletas.objects.all()
    serializer_class = ColetasSerializer
    # permission_classes = [IsAuthenticated]


class EnderecosViewSet(viewsets.ModelViewSet):
    queryset = Enderecos.objects.all()
    serializer_class = EnderecosSerializer
    # permission_classes = [IsAuthenticated]


class MateriaisViewSet(viewsets.ModelViewSet):
    queryset = Materiais.objects.all()
    serializer_class = MateriaisSerializer
    # permission_classes = [IsAuthenticated]


class MateriaisParceirosViewSet(viewsets.ModelViewSet):
    queryset = MateriaisParceiros.objects.all()
    serializer_class = MateriaisParceirosSerializer
    # permission_classes = [IsAuthenticated]


class MateriaisPontosColetaViewSet(viewsets.ModelViewSet):
    queryset = MateriaisPontosColeta.objects.all()
    serializer_class = MateriaisPontosColetaSerializer
    # permission_classes = [IsAuthenticated]


class PagamentosViewSet(viewsets.ModelViewSet):
    queryset = Pagamentos.objects.all()
    serializer_class = PagamentosSerializer
    # permission_classes = [IsAuthenticated]


class PontosColetaViewSet(viewsets.ModelViewSet):
    queryset = PontosColeta.objects.all()
    serializer_class = PontosColetaSerializer
    # permission_classes = [IsAuthenticated]


class SolicitacoesViewSet(viewsets.ModelViewSet):
    queryset = Solicitacoes.objects.all()
    serializer_class = SolicitacoesSerializer
    # permission_classes = [IsAuthenticated]


class TelefonesViewSet(viewsets.ModelViewSet):
    queryset = Telefones.objects.all()
    serializer_class = TelefonesSerializer
    # permission_classes = [IsAuthenticated]
>>>>>>> Stashed changes
