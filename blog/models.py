from django.db import models

# Create your models here.

from django.db import models


class Postagem(models.Model):

    class Meta:
        verbose_name_plural = 'Postagens'

    autor = models.ForeignKey('Autor', on_delete=models.CASCADE)
    titulo = models.CharField('Título', max_length=100, help_text='O título deverá ter no máximo 100 caractéres')
    texto = models.TextField('Texto')
    data_criacao = models.DateTimeField(auto_now=True)
    data_publicacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo


class Autor(models.Model):

    class Meta:
        verbose_name_plural = 'Autores'

    nome = models.CharField('Nome', max_length=100)
    telefone = models.CharField('Telefone', max_length=10, null=True, blank=False)
    data_criacao = models.DateTimeField(auto_now=True)
    email = models.EmailField('Email')

    def __str__(self):
        return self.nome
