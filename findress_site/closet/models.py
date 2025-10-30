# Em findress_site/closet/models.py

from django.db import models
from django.contrib.auth.models import User # Importa o User padrão do Django

class PecaRoupa(models.Model):
    # Corresponde a id_usuario no seu diagrama
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_peca = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    cor = models.CharField(max_length=50)
    tamanho = models.CharField(max_length=20)
    imagem = models.ImageField(upload_to='pecas/', null=True, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome_peca} ({self.usuario.username})"

class Look(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_look = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    # Relação Muitos-para-Muitos através da tabela LookPeca
    pecas = models.ManyToManyField(PecaRoupa, through='LookPeca')

    def __str__(self):
        return self.nome_look

class LookPeca(models.Model):
    look = models.ForeignKey(Look, on_delete=models.CASCADE)
    peca = models.ForeignKey(PecaRoupa, on_delete=models.CASCADE)

class Gostar(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    look = models.ForeignKey(Look, on_delete=models.CASCADE)
    data_gosto = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Garante que um usuário só pode curtir um look uma vez
        unique_together = ('usuario', 'look')