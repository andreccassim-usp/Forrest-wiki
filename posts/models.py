from django.db import models
from django.conf import settings


class Categoria(models.Model):
    nome = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nome


class Posts(models.Model):
    name = models.CharField(max_length=255)
    categorias = models.ManyToManyField(Categoria, related_name="posts")
    conteudo = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Exibe nome + lista de categorias
        cats = ", ".join(c.nome for c in self.categorias.all())
        return f'{self.name} ({cats})'


class Comentarios(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'"{self.text}" - {self.author.username}'