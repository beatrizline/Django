from django.db import models

SEXO_CHOICES = (
    ('M', 'Masculino'), 
    ('F', 'Feminino')
)

class Aluno(models.Model):
    nome = models.CharField(max_length=250)
    foto = models.ImageField(null=True)
    sexo = models.CharField(choices=SEXO_CHOICES, max_length=32) 
    dt_nasc = models.DateField(default=False)
    telefone = models.IntegerField(default=False)
    cpf = models.IntegerField(default=False, max_length=12)