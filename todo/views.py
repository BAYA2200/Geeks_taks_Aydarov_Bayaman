from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from todo.models import Task
from todo.serializers import TaskSerializer


class TaskAPIView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
