# Este é o conteúdo CORRETO para findress_site/closet/urls.py
# Este é o conteúdo CORRETO para findress_site/closet/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('todas/', views.listar_pecas, name='listar_pecas'),
    path('buscar/', views.pagina_busca, name='pagina_busca'),
    path('resultados/', views.resultado_busca, name='resultado_busca'),
]