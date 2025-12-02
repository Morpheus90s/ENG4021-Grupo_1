from django.shortcuts import render, redirect
from .models import PecaRoupa
# Importações necessárias para o login manual e cadastro
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm # <--- IMPORTANTE: Adicionado

# --- 1. PÁGINA INICIAL (Home) ---
def home(request):
    """Renderiza a página inicial com o banner e cards."""
    return render(request, 'closet/home.html')

# --- 2. LISTA COMPLETA (Página de Consulta) ---
def listar_pecas(request):
    """Mostra todas as peças cadastradas."""
    todas_as_pecas = PecaRoupa.objects.all()
    contexto = {
        'pecas': todas_as_pecas,
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

# --- 6. MEU PERFIL ---
def perfil(request):
    """Renderiza a página de perfil do usuário."""
    return render(request, 'closet/perfil.html')

# --- 7. LOGIN MÁGICO (BYPASS) ---
def entrar(request):
    """
    Simula um login. Se for POST (clicou no botão),
    loga o primeiro usuário do banco automaticamente.
    """
    if request.method == 'POST':
        # Pega o primeiro usuário que encontrar (geralmente o admin)
        usuario_magico = User.objects.first()
        
        if usuario_magico:
            # Força o login desse usuário
            login(request, usuario_magico)
            
            # Redireciona para a home para atualizar o menu
            return redirect('home')
            
    # Se for GET (apenas abriu a página), mostra o formulário
    return render(request, 'registration/login.html')

# --- 8. CADASTRO (NOVA FUNÇÃO) ---
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