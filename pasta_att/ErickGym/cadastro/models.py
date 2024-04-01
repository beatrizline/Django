from django.db import models


class Alunos(models.Model):
    SEXO_CHOICES = (
    ('M', 'Masculino'), 
    ('F', 'Feminino'),
)

    nome = models.CharField(max_length=250, null=False, blank=False)
    foto = models.ImageField(null=True)
    sexo = models.CharField(choices=SEXO_CHOICES, max_length=1) 
    dt_nasc = models.DateField()
    telefone = models.CharField(max_length=14, blank=False, null=False)
    cpf = models.CharField(max_length=14, blank=False, null=False)