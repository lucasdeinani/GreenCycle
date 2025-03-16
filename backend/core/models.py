from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    telefone = models.CharField(max_length=15, blank=True, null=True)
    endereco = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username

class MaterialDescarte(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    categoria = models.CharField(max_length=100)
    ponto_coleta = models.CharField(max_length=255)
    reciclavel = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
