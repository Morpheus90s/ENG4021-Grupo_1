
from django.urls import path
from . import views

urlpatterns = [
   
    path('pecas/', views.listar_pecas, name='lista_pecas'),
    
    path('busca/', views.pagina_busca, name='pagina_busca'),
    
    path('resultado/', views.resultado_busca, name='resultado_busca'),
]