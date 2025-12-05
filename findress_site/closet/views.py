from django.shortcuts import render, redirect
from .models import PecaRoupa
# Importações necessárias para o login e cadastro
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# IMPORTANTE: Importamos o decorador para proteger a página
from django.contrib.auth.decorators import login_required

# --- 1. PÁGINA INICIAL (Home) ---
def home(request):
    """Renderiza a página inicial com o banner e cards."""
    return render(request, 'closet/home.html')

# --- 2. LISTA "MEU CLOSET" (Agora Filtrada) ---
@login_required # Só quem está logado pode acessar
def listar_pecas(request):
    """
    Mostra APENAS as peças cadastradas pelo usuário logado.
    """
    # request.user contém o usuário atual que está logado.
    # Filtramos a tabela PecaRoupa para pegar apenas onde o campo 'usuario' é igual ao logado.
    # OBS: Certifique-se de que o modelo PecaRoupa tem o campo 'usuario'.
    minhas_pecas = PecaRoupa.objects.filter(usuario=request.user)
    
    contexto = {
        'pecas': minhas_pecas,
        'busca': None, 
    }
    return render(request, 'closet/lista_pecas.html', contexto)

# --- 3. FORMULÁRIO DE BUSCA ---
def pagina_busca(request):
    """Mostra apenas o formulário para digitar a busca."""
    return render(request, 'closet/pagina_busca.html')

# --- 4. RESULTADOS DA BUSCA ---
def resultado_busca(request):
    """Recebe o termo, filtra o banco e reutiliza a lista para mostrar."""
    busca_digitada = request.GET.get('busca', '')

    if busca_digitada:
        # Opcional: Se quiser que a busca também seja restrita ao usuário, use:
        # pecas_filtradas = PecaRoupa.objects.filter(usuario=request.user, nome_peca__icontains=busca_digitada)
        pecas_filtradas = PecaRoupa.objects.filter(nome_peca__icontains=busca_digitada)
    else:
        pecas_filtradas = PecaRoupa.objects.none()

    contexto = {
        'pecas': pecas_filtradas,
        'busca': busca_digitada,
    }
    return render(request, 'closet/lista_pecas.html', contexto)

# --- 5. SOBRE A MARCA ---
def sobre(request):
    """Renderiza a página de texto 'Sobre'."""
    return render(request, 'closet/sobre.html')

# --- 6. PÁGINA DE AJUDA ---
def pagina_ajuda(request):
    """Renderiza a página de ajuda/FAQ."""
    return render(request, 'closet/ajuda.html')

# --- 7. PÁGINA DE CONTATO ---
def pagina_contato(request):
    """Renderiza a página de contato."""
    return render(request, 'closet/contato.html')

# --- 8. MEU PERFIL ---
@login_required
def perfil(request):
    """Renderiza a página de perfil do usuário."""
    return render(request, 'closet/perfil.html')

# --- 9. LOGIN MÁGICO (Mantido conforme seu código) ---
def entrar(request):
    """
    Simula um login. Se for POST, loga o primeiro usuário do banco.
    """
    if request.method == 'POST':
        usuario_magico = User.objects.first()
        if usuario_magico:
            login(request, usuario_magico)
            return redirect('home')
            
    return render(request, 'registration/login.html')

# --- 10. CADASTRO ---
def cadastrar(request):
    """Exibe o formulário de cadastro e cria o usuário."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/cadastro.html', {'form': form})