from django.urls import path
from . import views

urlpatterns = [
    # 0. ROTA DA HOME
    path('', views.home, name='home'),

    # 1. Lista Completa
    path('pecas/', views.listar_pecas, name='lista_pecas'),
    
    # 2. Formulário de Busca
    path('busca/', views.pagina_busca, name='pagina_busca'),
    
    # 3. Resultados da Busca
    path('resultado/', views.resultado_busca, name='resultado_busca'),

    # 4. Sobre a Marca
    path('sobre/', views.sobre, name='sobre'),

    # 5. Meu Perfil
    path('perfil/', views.perfil, name='perfil'),

    # 6. CADASTRO
    path('cadastro/', views.cadastrar, name='cadastro'),
    
]