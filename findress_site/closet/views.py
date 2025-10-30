from django.shortcuts import render
from .models import PecaRoupa # Importa o modelo que queremos consultar

# --- Esta é a view que você já tinha ---
def listar_pecas(request):
    """
    Esta view (lógica) busca todas as peças de roupa cadastradas no banco
    e as envia para o template HTML 'closet/lista_pecas.html'.
    """
    todas_as_pecas = PecaRoupa.objects.all()

    contexto = {
        'pecas': todas_as_pecas,
    }
    
    return render(request, 'closet/lista_pecas.html', contexto)

# --- AQUI COMEÇA A NOVA TAREFA: "Consulta com filtro" ---

# 1. View para MOSTRAR a página com o formulário de busca
def pagina_busca(request):
    """
    Esta view apenas renderiza o template que contém o formulário de busca.
    """
    return render(request, 'closet/pagina_busca.html')


# 2. View para PROCESSAR a busca e MOSTRAR OS RESULTADOS
def resultado_busca(request):
    """
    Esta view recebe o que o usuário digitou no formulário,
    filtra o banco de dados e envia os resultados para o template.
    """
    
    # Pega o valor do campo 'busca' do formulário (via método GET)
    # Se não encontrar nada, usa uma string vazia ''
    busca_digitada = request.GET.get('busca', '')

    # Filtra o banco de dados
    # PecaRoupa.objects.filter(nome_peca__icontains=busca_digitada)
    # __icontains significa: "contenha este texto, ignorando maiúsculas/minúsculas"
    if busca_digitada:
        pecas_filtradas = PecaRoupa.objects.filter(nome_peca__icontains=busca_digitada)
    else:
        pecas_filtradas = PecaRoupa.objects.all() # Se a busca for vazia, mostra tudo

    contexto = {
        'pecas': pecas_filtradas, # Envia os resultados para o template
        'busca': busca_digitada,  # Envia o termo da busca de volta (para sabermos o que foi buscado)
    }

    # Reutiliza o mesmo template da lista de peças para mostrar os resultados
    return render(request, 'closet/lista_pecas.html', contexto)

