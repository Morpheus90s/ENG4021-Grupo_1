from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import PecaRoupa

@login_required
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
    
    # CORREÇÃO AQUI:
    # Apontar para o template correto, que está em 'closet/closet.html'
    # (Baseado na sua estrutura de arquivos e no erro TemplateDoesNotExist)
    return render(request, 'closet/closet.html')

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
    
    # CORREÇÃO AQUI:
    # Esta view deve mostrar a lista de resultados,
    # então usamos 'closet/lista_pecas.html' (o mesmo de 'listar_pecas')
    # e passamos o 'contexto' com os resultados.
    return render(request, 'closet/lista_pecas.html', contexto)