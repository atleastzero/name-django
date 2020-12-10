from django.shortcuts import render
from rest_framework import viewsets

from .serializers import TodoSerializer, RoutineSerializer
from .models import Todo, Routine

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    

class RoutineView(viewsets.ModelViewSet):
    serializer_class = RoutineSerializer
    queryset = Routine.objects.all()