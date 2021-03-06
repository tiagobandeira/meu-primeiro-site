from django.db import models
from django.utils import timezone
# Create your models here.

class PostFilmes(models.Model):
    titulo = models.CharField(max_length=100)
    filme = models.CharField(max_length=100)
    autor = models.ForeignKey('auth.User')
    descricao = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now)
    data_publicacao = models.DateTimeField(blank= True, null=True)

    def Publica(self):
        self.data_publicacao = timezone.now()
        self.save()
    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    autor = models.CharField(max_length=100)
    texto = models.TextField()
    email = models.CharField(max_length=100)
    post_id = models.ForeignKey(PostFilmes)
    def Comenta(self):
        self.save()
    def __str__(self):
        return self.autor
    
    
