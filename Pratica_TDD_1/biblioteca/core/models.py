from django.db import models

class LivroModel(models.Model):
    titulo = models.CharField('titulo', max_length=200)
    editora = models.CharField('editora', max_length=200)
    autor = models.CharField('autor', max_length=200)
    isbn = models.CharField('isbn', max_length=200)
    paginas = models.CharField('paginas', max_length=200)
    edicao = models.CharField('edicao', max_length=200)

modificado_em = models.DateTimeField(
        verbose_name='modificado em',
        auto_now_add=False, auto_now=True)

def __str__(self):
        return self.titulo