from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from treinos.models import Exercicio
from treinos.serializers import ExercicioSerializer


class ListaExerciciosView(APIView):

    def get(self, request):
        exercicios = Exercicio.objects.all()
        serializer = ExercicioSerializer(exercicios, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = ExercicioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)




//////////////


#from rest_framework.views import APIView
#from rest_framework.response import Response
#from alunos.serializers import AlunosSerializer
#from alunos.models import Alunos
#from django.http import Http404
#from rest_framework import status

#class ListCreateAlunos(APIView):

    #def get(self, request):
        #alunos = Alunos.objects.all()
        #serializer = AlunosSerializer(alunos, many=True)
        #return Response(serializer.data, status=200)
    
    #def post(self, request):
        #serializer = AlunosSerializer(data=request.data)
        #if serializer.is_valid():
            #serializer.save()
            #return Response(serializer.data, status=201)
        #else:
            #return Response(serializer.errors, status=400)


#class DetalheAlunos(APIView):
    #def get_aluno(self, apk):
        #try:
            #return Alunos.objects.get()
        #except Alunos.DoesNotExist:
            #raise Http404
        
        
    #def get(self,request,pk):
        #aluno = self.get_aluno(pk)
        #serializer = AlunosSerializer(aluno,data=request.data)
        #if serializer.is_valid():
            #serializer.save()
            #return Response(serializer.data)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #def delete(self,request,pk):
        #aluno = self.get_aluno(pk)
        #aluno.delete()
        #return Response(status=status.HTTP_204_NO_CONTENT)
    


# Parte de Exercicios

#class DeleteAlunosView(APIView):
    
    #def get_object(self, pk):
        #try:
            #exercicio = Exercicio.objects.get(pk=pk)
           # return exercicio
     #   except Exercicio.DoesNotExist:
          #  raise Http404

   # def get(self, request, pk):
     #   exercicio = self.get_object(pk)
      #  serializer = ExercicioSerializer(instance=exercicio)
      #  return Response(data=serializer.data, status=status.HTTP_200_OK)

  #  def delete(self,request, pk):
      #  try:
          #  exercicio = Exercicio.objects.get(pk=pk)
         #   exercicio.delete()
          #  return Response(status=status.HTTP_204_NO_CONTENT)
       # except Exercicio.DoesNotExit:
           # raise Http404
        
   # def put(self,request,pk):
      #  exercicio = self.get_object(pk)
      #  serializer = ExercicioSerializer(instance=exercicio, data=request.data)
      #  if serializer_is_valid():
        #    serializer.save()
       #     return Response(serializer.data)
      #  else:
          #  return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
            
        
