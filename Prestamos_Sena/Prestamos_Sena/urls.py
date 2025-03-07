"""
URL configuration for Prestamos_Sena project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

# Importamos las vistas desde app
from App import views
from App.Views.Registro import registroViews
from App.Views.Prestamos import prestamoViews
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    # Esta ruta estara vacia para que sea la pagina principal
    path('', views.index, name='index'),
    path('acceso/', views.index, name='acceso'),
    path('registro/', registroViews.registro, name='registro'),
    path('registro/', views.registro, name='registro'),
    path('registrar/', registroViews.registrar, name='guardar_registro'),
    
    path('prestamos/', prestamoViews.prestamos, name='prestamos'),
    path('guardar_prestamo/', prestamoViews.guardar_prestamo, name='guardar_prestamo'),
    path('devoluciones/', views.devoluciones, name='devoluciones'),
    path('inventario/', views.inventario, name='inventario'),
    path('home/', views.home, name='home'),

]