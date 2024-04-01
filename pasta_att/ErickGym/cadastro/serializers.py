from rest_framework.serializers import ModelSerializer
from cadastro.models import Alunos

class AlunosSerializer(ModelSerializer):
    class Meta:
        model = Alunos
        fields=['nome', 'foto', 'sexo', 'dt_nasc', 'telefone', 'cpf']