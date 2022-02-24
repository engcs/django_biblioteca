from django.db import models
from datetime import date
# Create your models here.

class Livros(models.Model):
    nome = models.CharField(max_length=100, blank=True)
    autor = models.CharField(max_length=30, blank=True)
    data_cadastro = models.DateField(default=date.today)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Livros"
