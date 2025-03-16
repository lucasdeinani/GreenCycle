from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, MaterialDescarteViewSet

router = DefaultRouter()
router.register(r'usuarios', CustomUserViewSet)
router.register(r'materiais', MaterialDescarteViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Inclui as rotas da API
]