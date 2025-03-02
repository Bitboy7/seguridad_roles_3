"""
URL configuration for seguridad_roles_3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView  # Importa RedirectView
from usuarios.views import inicio, registro, inicio_sesion  # Importa las vistas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('', RedirectView.as_view(url='/registro/')),  # Redirige la ruta raíz a /registro
    path('registro/', registro, name='registro'),  # Ruta para el registro
    path('login/', inicio_sesion, name='login'),  # Ruta para el inicio de sesión
]
