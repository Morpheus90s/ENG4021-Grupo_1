from django.urls import path
from . import views

# Este arquivo aponta para as suas 3 funções no views.py
# Ele NÃO PODE ter 'include()'

urlpatterns = [
    # 1. Aponta para a sua view 'listar_pecas'
    # URL: /pecas/
    path('pecas/', views.listar_pecas, name='lista_pecas'),
    
    # 2. Aponta para a sua view 'pagina_busca'
    # URL: /busca/
    path('busca/', views.pagina_busca, name='pagina_busca'),
    
    # 3. Aponta para a sua view 'resultado_busca'
    # URL: /resultado/
    path('resultado/', views.resultado_busca, name='resultado_busca'),
]