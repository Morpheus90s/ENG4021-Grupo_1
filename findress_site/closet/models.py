from django.db import models
# Usaremos o sistema de usuários padrão do Django, que já tem nome, email e senha.
from django.contrib.auth.models import User

# --- Corresponde à sua tabela "peca_roupa" ---
class PecaRoupa(models.Model):
    # id_peca é criado automaticamente pelo Django (como "id")
    # id_usuario é o ForeignKey para o User
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_peca = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    cor = models.CharField(max_length=50)
    tamanho = models.CharField(max_length=20, blank=True)
    imagem = models.ImageField(upload_to='pecas/', null=True, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''
        Isso define como a PecaRoupa vai aparecer na área de admin
        (assim como o exemplo "return 'Pessoa: ' + self.nome")
        '''
        return f"{self.nome_peca} (de {self.usuario.username})"

# --- Corresponde à sua tabela "Look" ---
class Look(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_look = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    # Relação Muitos-para-Muitos através da tabela LookPeca
    pecas = models.ManyToManyField(PecaRoupa, through='LookPeca')

    def __str__(self):
        return self.nome_look

# --- Corresponde à sua tabela "Look_peca" (Tabela de Junção) ---
class LookPeca(models.Model):
    look = models.ForeignKey(Look, on_delete=models.CASCADE)
    peca = models.ForeignKey(PecaRoupa, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.look.nome_look} - {self.peca.nome_peca}"

# --- Corresponde à sua tabela "gostar" ---
class Gostar(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    look = models.ForeignKey(Look, on_delete=models.CASCADE)
    data_gosto = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Garante que um usuário só pode curtir um look uma vez
        unique_together = ('usuario', 'look')
