from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from cadastro.serializers import AlunosSerializer
from .models import Alunos
from rest_framework.generics import ListCreateAPIView

class ListCreateAlunoView(APIView):
    queryset = Alunos.objects.all()
    serializer_class = AlunosSerializer

#class DetailUpdateDeleteAlunosView(RetrieveUpdateDestroyAPIView):

