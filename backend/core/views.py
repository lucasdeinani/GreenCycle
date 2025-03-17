from rest_framework import generics, viewsets, permissions
from .models import CustomUser, MaterialDescarte
from .serializers import CustomUserSerializer, MaterialDescarteSerializer
from django.http import JsonResponse

class CustomUserListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class CustomUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

class MaterialDescarteViewSet(viewsets.ModelViewSet):
    queryset = MaterialDescarte.objects.all()
    serializer_class = MaterialDescarteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:  # Permite GET sem autenticação
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]  # Exige login para POST, PUT, DELETE

def home(request):
    return JsonResponse({"message": "Bem-vindo ao backend da nossa aplicação!"})
