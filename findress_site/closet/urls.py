from django.urls import path
from . import views # Importa o views.py do app

urlpatterns = [
    # Quando o usuário acessar a URL 'pecas/', o Django vai chamar
    # a função 'listar_pecas' que você criou no views.py
    path('pecas/', views.listar_pecas, name='lista_pecas'),
]
