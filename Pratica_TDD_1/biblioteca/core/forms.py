from django import forms
from django.core.exceptions import ValidationError
from core.models import LivroModel


def validate_title(value):
    if len(value) < 3:  
        raise ValidationError('Deve ter pelo menos tres caracteres o titulo')
    
def validate_editora(value):
    if len(value) < 3:  
        raise ValidationError('Deve ter pelo menos tres caracteres a editora')
    
def validate_autores(value):
    if len(value) < 10:
        raise ValidationError('Deve ter pelo menos dez caracteres o nome do Autor')
    
def validate_edicao(value):
    if len(value) < 3:  
        raise ValidationError('Deve ter pelo menos tres caracteres a editora')
    
def validate_isbn(value):
    try:
        isbn = int(value)
    except ValueError:
        raise ValidationError('A página deve ser um número inteiro.')
    if not (isbn > 13):
        raise ValidationError('O número do ISBN tem que ter 13 caracteres.')

def validate_pagina(value):
    try:
        pagina = int(value)
    except ValueError:
        raise ValidationError('A página deve ser um número inteiro.')
    if not (pagina >  3):
        raise ValidationError('O número de páginas deve estar entre 1 e 3.')
   
class LivroForm(forms.ModelForm):

    class Meta:
        model = LivroModel
        fields = ['titulo', 'editora', 'autor', 'isbn', 'paginas', 'edicao']
        error_messages = {
            'titulo': {
                'required': ("Informe o título do livro."),
            },
            'editora': {
                'required': ("Informe a editora do livro."),
            },
            'autor': {
                'required': ("Informe a autor do livro."),
            },
            'isbn': {
                'required': ("Informe a ISBN do livro."),
            },
            'paginas': {
                'required': ("Informe a paginas do livro."),
            },
            'edicao': {
                'required': ("Informe a edição do livro."),
            }
        }

    def clean_titulo(self):
        titulo = self.cleaned_data['titulo']
        validate_title(titulo)
        return titulo

    def clean_editora(self):
        editora = self.cleaned_data['editora']
        validate_editora(editora)
        return editora
    
    def clean_autor(self):
        autor = self.cleaned_data['autor']
        validate_autores(autor)
        return autor
    
    def clean_isbn(self):
        isbn = self.cleaned_data['isbn']
        validate_isbn(isbn)
        return isbn
    
    def clean_edicaos(self):
        edicao = self.cleaned_data['edicao']
        validate_edicao(edicao)
        return edicao
    
    def clean_paginas(self):
        paginas = self.cleaned_data['paginas']
        validate_pagina(paginas)
        return paginas
    
    def clean(self):
        self.cleaned_data = super().clean()
        return self.cleaned_data

