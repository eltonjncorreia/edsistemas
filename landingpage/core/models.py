from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
class Contato(models.Model):
    nome = models.CharField('Nome', max_length=255)
    email = models.EmailField('Email', max_length=255)
    mensagem = models.TextField()
    telefone = models.CharField('Telefone',
                                max_length=11,
                                null=True,
                                blank=True,
                                validators=[RegexValidator(r'^(\d+)$')])
