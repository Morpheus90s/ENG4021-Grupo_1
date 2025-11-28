from django.urls import path
from . import views

urlpatterns = [
    # --- PEÇAS ---
    path('todas/', views.listar_pecas, name='listar_pecas'),
    path('buscar/', views.pagina_busca, name='pagina_busca'),
    path('resultados/', views.resultado_busca, name='resultado_busca'),
    path('adicionar_peca/', views.adicionar_peca, name='adicionar_peca'),
    
    # --- LOOKS ---
    path('adicionar_look/', views.adicionar_look, name='adicionar_look'),
    
    # --- FEED SOCIAL ---
    path('feed/', views.feed_looks, name='feed_looks'),
    
    # --- AUTENTICAÇÃO ---
    path('cadastro/', views.register, name='register'),
    
    # --- HOME ---
    # (Esta linha é importante para o link do logotipo funcionar)
    path('', views.home, name='home'),
]