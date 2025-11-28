from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import PecaRoupa, Look, LookPeca

# --- AUTENTICAÇÃO ---
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('listar_pecas')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# --- PEÇAS ---
@login_required
def listar_pecas(request):
    pecas = PecaRoupa.objects.filter(usuario=request.user)
    return render(request, 'closet/lista_pecas.html', {'pecas': pecas})

@login_required
def pagina_busca(request):
    return render(request, 'closet/closet.html')

@login_required
def resultado_busca(request):
    busca = request.GET.get('busca', '')
    if busca:
        pecas = PecaRoupa.objects.filter(usuario=request.user, nome_peca__icontains=busca)
    else:
        pecas = PecaRoupa.objects.none()
    return render(request, 'closet/lista_pecas.html', {'pecas': pecas, 'busca': busca})

@login_required
def adicionar_peca(request):
    if request.method == 'POST':
        PecaRoupa.objects.create(
            usuario=request.user,
            nome_peca=request.POST.get('nome_peca'),
            categoria=request.POST.get('categoria'),
            cor=request.POST.get('cor'),
            tamanho=request.POST.get('tamanho'),
            imagem=request.FILES.get('imagem_peca')
        )
        return redirect('listar_pecas')
    return render(request, 'closet/adicionar_peca.html')

# --- LOOKS ---
@login_required
def adicionar_look(request):
    if request.method == 'POST':
        # 1. Cria o objeto Look base
        novo_look = Look.objects.create(
            usuario=request.user,
            nome_look=request.POST.get('nome_look'),
            descricao=request.POST.get('descricao')
        )

        # 2. Pega a lista de IDs das peças selecionadas
        pecas_ids = request.POST.getlist('pecas')

        # OTIMIZAÇÃO: Usa bulk_create para salvar tudo de uma vez
        relacoes = []
        for pid in pecas_ids:
            peca = get_object_or_404(PecaRoupa, id=pid, usuario=request.user)
            relacoes.append(LookPeca(look=novo_look, peca=peca))
        
        LookPeca.objects.bulk_create(relacoes)
        
        return redirect('listar_pecas')

    else:
        pecas = PecaRoupa.objects.filter(usuario=request.user)
        return render(request, 'closet/adicionar_look.html', {'pecas_disponiveis': pecas})

@login_required
def feed_looks(request):
    """Mostra looks de TODOS os utilizadores (menos o meu)."""
    
    # OTIMIZAÇÃO CRÍTICA
    looks_do_feed = Look.objects.exclude(usuario=request.user)\
                                .select_related('usuario')\
                                .prefetch_related('pecas')\
                                .order_by('-data_criacao')
    
    return render(request, 'closet/feed_looks.html', {'looks': looks_do_feed})