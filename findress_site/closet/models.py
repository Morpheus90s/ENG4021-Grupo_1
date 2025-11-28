from django.db import models
from django.contrib.auth.models import User

# --- Tabela de Peças de Roupa ---
class PecaRoupa(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_peca = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    cor = models.CharField(max_length=50)
    tamanho = models.CharField(max_length=20, blank=True)
    imagem = models.ImageField(upload_to='pecas/', null=True, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome_peca} ({self.usuario.username})"

# --- Tabela de Looks ---
class Look(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_look = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    foto_principal = models.ImageField(upload_to='looks/', blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    # Relação Muitos-para-Muitos usando a tabela intermédia LookPeca
    pecas = models.ManyToManyField(PecaRoupa, through='LookPeca', related_name='looks')

    def __str__(self):
        return self.nome_look

# --- Tabela Intermédia (Look <-> Peça) ---
class LookPeca(models.Model):
    look = models.ForeignKey(Look, on_delete=models.CASCADE)
    peca = models.ForeignKey(PecaRoupa, on_delete=models.CASCADE)
    data_adicao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.look.nome_look} - {self.peca.nome_peca}"

# --- Tabela de Curtidas (Para o Feed Social) ---
class Gostar(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    look = models.ForeignKey(Look, on_delete=models.CASCADE)
    data_gosto = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'look') # Evita curtir