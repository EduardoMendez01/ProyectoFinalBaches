"""
URL configuration for reporteCuidadano project.

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
from portalWeb import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('iniciarSecion/', views.iniciarSesion, name='iniciarSecion'),
    path('registrarse/', views.registrar, name='registrarse'),
    path('admin/', admin.site.urls),
    path('menu/', views.menu, name='menu'),
    path('hacerReportes/', views.hacerReportes, name='hacerReportes'),
    path('verReportes/', views.verReportes, name='verReportes'),
    path('menuAdmin/', views.menuAdmin, name='menuAdmin'),
    path('inicioSecionAdmin/', views.iniciarSecionAdmin, name="inicioSecionAdmin"),
    path('verReportesAdmin/', views.verReportesAdmin, name="verReportesAdmin"),
    path('verReportesAdmin/editarReporte/<int:codigo>/', views.editarReporte, name='editarReporte'),
    path('editarReporte/', views.editarReporte, name="editarReporte"),
    path('verReportesAdmin/VisualizarReportesAdmin/<int:codigo>/', views.VisualizarReportesAdmin, name="visualizarReporteAdmin")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)