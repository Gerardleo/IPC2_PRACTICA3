import practica3.view as view


"""
URL configuration for practica3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

urlpatterns = [
    path('', view.index, name='index'),
    path('admin/', admin.site.urls),
    path('cargarArchivo/', view.CargarArchivo, name='cargarArchivo'),
    path('cargarArchivoMascotas/', view.cargarArchivoMascotas, name='cargarArchivoMascotas'),
    path('procesarDatos/', view.procesarDatos, name='procesarDatos'),
    path('procesarDatosSalida/', view.procesarDatosSalida, name='procesarDatosSalida'),
    path('datosPersonales/', view.datosPersonales, name='datosPersonales'),
    path('borrarDatos/', view.borrarDatos, name='borrarDatos'),
    path('borrar/', view.borrar_Datos, name='borrar')

]
