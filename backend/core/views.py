from rest_framework import generics, viewsets
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

class MaterialDescarteViewSet(viewsets.ModelViewSet):
    queryset = MaterialDescarte.objects.all()
    serializer_class = MaterialDescarteSerializer

def home(request):
    return JsonResponse({"message": "Bem-vindo ao backend da nossa aplicação!"})
