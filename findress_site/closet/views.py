from django.shortcuts import render
from .models import PecaRoupa

def listar_pecas(request):
    """Mostra todas as peças."""
    todas_as_pecas = PecaRoupa.objects.all()
    contexto = {
        'pecas': todas_as_pecas,
        'busca': None,  
    }
    return render(request, 'closet/lista_pecas.html', contexto)

def pagina_busca(request):
    """Mostra a página com o formulário de busca."""
    return render(request, 'closet/pagina_busca.html')

def resultado_busca(request):
    """Recebe a busca, filtra o banco e mostra os resultados."""
    busca_digitada = request.GET.get('busca', '')

    if busca_digitada:
        pecas_filtradas = PecaRoupa.objects.filter(nome_peca__icontains=busca_digitada)
    else:
        pecas_filtradas = PecaRoupa.objects.none()

    contexto = {
        'pecas': pecas_filtradas,
        'busca': busca_digitada,
    }
    
    return render(request, 'closet/lista_pecas.html', contexto)