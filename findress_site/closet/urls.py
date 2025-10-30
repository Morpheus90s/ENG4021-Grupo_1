from django.urls import path
from . import views

urlpatterns = [
    # Rota da tarefa anterior (Lista Completa)
    path('pecas/', views.listar_pecas, name='lista_pecas'),
    
    # --- Novas Rotas para a "Consulta com filtro" ---
    
    # 1. Rota para a página que MOSTRA o formulário de busca
    path('busca/', views.pagina_busca, name='pagina_busca'),
    
    # 2. Rota que RECEBE a busca e mostra os resultados
    path('resultado/', views.resultado_busca, name='resultado_busca'),
]