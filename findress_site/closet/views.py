from django.shortcuts import render
# Importa o modelo PecaRoupa que você definiu na "Base de Dados"
from .models import PecaRoupa

# Esta é a função que o roteiro pede, adaptada para seu projeto
def listar_pecas(request):
    """
    Esta view busca todas as peças de roupa do banco
    e as envia para o template 'lista_pecas.html'.
    """
    
    # 1. Busca todos os objetos PecaRoupa no banco
    todas_as_pecas = PecaRoupa.objects.all()

    # 2. Cria um "contexto" para enviar os dados para o HTML
    contexto = {
        'pecas': todas_as_pecas, # 'pecas' é o nome que usaremos no HTML
    }
    
    # 3. Renderiza o template, passando os dados do contexto
    return render(request, 'closet/lista_pecas.html', contexto)
