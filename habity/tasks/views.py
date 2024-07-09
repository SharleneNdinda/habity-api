from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from habity.tasks.models import Task
from habity.tasks.filters import TaskFilter
from habity.tasks.serializers import TaskSerializer


class TaskViewSet(ModelViewSet):
    """Task ViewSet."""

    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    filterset_class = TaskFilter
