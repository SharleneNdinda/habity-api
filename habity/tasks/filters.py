from django_filters import FilterSet 

from habity.tasks.models import Task


class TaskFilter(FilterSet):
    class Meta:
        model = Task
        fields = "__all__"
