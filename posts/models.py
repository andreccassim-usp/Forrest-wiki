from django.db import models
from django.conf import settings


class Posts(models.Model):
    name = models.CharField(max_length=255)
    categoria = models.CharField(max_length=255)
    conteudo = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.name} ({self.categoria})'


class Comentarios(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'"{self.text}" - {self.author.username}'