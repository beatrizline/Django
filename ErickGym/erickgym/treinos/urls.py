from django.urls import path
from treinos.views import(
    ListCreateExerciciosView,
    DetailUpdateDeleteExerciciosView)

urlpatterns = [
    path('treinos', ListCreateExerciciosView.as_view()),
    path('treinos/<int:pk>', DetailUpdateDeleteExerciciosView.as_view()),
]
