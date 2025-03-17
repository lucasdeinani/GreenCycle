from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, MaterialDescarteViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'usuarios', CustomUserViewSet)
router.register(r'materiais', MaterialDescarteViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Inclui as rotas da API
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]