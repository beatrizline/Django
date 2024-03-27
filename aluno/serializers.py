from rest_framework.serializers import ModelSerializer
from aluno.models import Aluno

class AlunoSerializer(ModelSerializer):
    class Meta:
        model = Aluno
        fields=['nome', 'foto', 'sexo', 'dt_nasc', 'telefone', 'cpf']