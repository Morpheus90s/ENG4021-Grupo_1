from django.shortcuts import render

# Create your views here.
# Em findress_site/closet/views.py

from django.shortcuts import render
from .models import PecaRoupa # Importa o modelo que queremos consultar

def listar_pecas(request):
    """
    Esta view busca todas as peças de roupa cadastradas no banco
    e as envia para um template HTML para serem exibidas.
    """
    todas_as_pecas = PecaRoupa.objects.all()

    contexto = {
        'pecas': todas_as_pecas,
    }
    
    return render(request, 'closet/lista_pecas.html', contexto)