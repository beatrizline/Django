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


class Clube(models.Model):
    nome = models.CharField(max_length=180)
    estado = models.CharField(choices=ESTADO_CHOICES,
                              max_length=120, null=True)
    cores = models.CharField(max_length=80, blank=True, null=True)
    ano_fundacao = models.PositiveIntegerField(default=0)
    tem_mundial = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
