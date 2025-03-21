from django.contrib import admin
from django.urls import path, include
from core.urls import urlpatterns

urlpatterns = [
    path('api/', include(urlpatterns)),
    path('auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
]
