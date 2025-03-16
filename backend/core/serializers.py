from rest_framework import serializers
from .models import CustomUser, MaterialDescarte

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'is_active', 'date_joined']

class MaterialDescarteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialDescarte
        fields = ['id', 'nome', 'descricao', 'categoria', 'ponto_coleta', 'reciclavel']