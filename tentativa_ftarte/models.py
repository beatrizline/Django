from django.db import models

ESTADO_CHOICES = (
    ('SP', 'São Paulo'),
    ('RJ', 'Rio de Janeiro'),
    ('MG', 'Minas Gerais'),
    ('RS', 'Rio Grande do Sul'),
    ('BA', 'Bahia'),
    ('PR', 'Paraná'),
    ('SC', 'Santa Catarina'),
    ('PE', 'Pernambuco'),
    ('CE', 'Ceará'),
    ('GO', 'Goiás'),
    ('PA', 'Pará'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('MA', 'Maranhão'),
    ('PB', 'Paraíba'),
    ('RN', 'Rio Grande do Norte'),
    ('AL', 'Alagoas'),
    ('PI', 'Piauí'),
    ('SE', 'Sergipe'),
    ('RO', 'Rondônia'),
    ('TO', 'Tocantins'),
    ('AC', 'Acre'),
    ('AP', 'Amapá'),
    ('RR', 'Roraima'),
)


DIVISAO_ATUAL = (
    ('A', 'Série A'),
    ('B', 'Série B'),
    ('C', 'Série C'),
    ('D', 'Série D'),
)


SEXO_CHOICES = (
    ('M', 'Masculino'),
    ('F', 'Feminino'),
)

class Clube(models.Model):
    nome = models.CharField(max_length=180)
    ano_fundacao = models.PositiveBigIntegerField(default=False)
    divisao_atual = models.CharField(choices=DIVISAO_ATUAL,max_length=1, null=True)
    image = models.ImageField(upload_to='images', null=True)
    sexo = models.CharField(choices=SEXO_CHOICES,max_length=32,null=True)
    competicao = models.CharField(max_length=32, default=False,choices=(('EST','Estadual'), ('NAC', 'Nacional'), ('INT', 'Internacional')))
    categoria = models.CharField(max_length=32, default=False,choices=(('COPA', 'Copa'), ('CAMP', 'Campeonato')))
    estado = models.CharField(choices=ESTADO_CHOICES,
                              max_length=120, null=True)
        

    def __str__(self):
        return self.nome
    
class Jogador(models.Model):
    nome = models.CharField(max_length=100)
    clube = models.ForeignKey(Clube, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Titulo(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.PositiveIntegerField()
    clube = models.ForeignKey(Clube, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} - {self.ano}"