# Em findress_site/closet/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Quando o usuário acessar a URL '/pecas/', a view 'listar_pecas' será chamada.
    # Este é o link para a sua Página de Consulta.
    path('pecas/', views.listar_pecas, name='lista_pecas'),
]