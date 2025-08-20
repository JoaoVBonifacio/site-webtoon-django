# webtoons/models.py
from django.db import models

class Webtoon(models.Model):
    STATUS_CHOICES = (
        ('em_andamento', 'Em Andamento'),
        ('concluido', 'Concluído'),
        ('hiato', 'Hiato'),
    )

    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    descricao = models.TextField()
    capa = models.ImageField(upload_to='capas/', help_text="A imagem de capa da webtoon")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='em_andamento')
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Capitulo(models.Model):
    webtoon = models.ForeignKey(Webtoon, related_name='capitulos', on_delete=models.CASCADE)
    numero = models.PositiveIntegerField()
    titulo = models.CharField(max_length=200, blank=True)
    data_publicacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-numero'] # Ordena do capítulo mais recente para o mais antigo

    def __str__(self):
        return f'{self.webtoon.titulo} - Cap. {self.numero}'
    
class Pagina(models.Model):
    capitulo = models.ForeignKey(Capitulo, related_name='paginas', on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='paginas/')
    ordem = models.PositiveIntegerField(help_text="A ordem da página no capítulo")

    class Meta:
        ordering = ['ordem'] # Garante que as imagens sempre apareçam na ordem correta

    def __str__(self):
        return f'Página {self.ordem} de {self.capitulo}'