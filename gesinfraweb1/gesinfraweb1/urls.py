# gesinfraweb/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inventario/', include('inventario.urls')),  # ← Agregar esta línea
    # O si quieres que sea la página principal:
    # path('', include('inventario.urls')),
]