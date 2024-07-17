from rest_framework.serializers import ModelSerializer

from habity.tasks.models import Task, TaskCategory


class TaskCategorySerializer(ModelSerializer):
    """Task Serializer."""

    class Meta:
        """Serialization options."""

        model = TaskCategory
        fields = "__all__"


class TaskSerializer(ModelSerializer):
    """Task Serializer."""

    category = TaskCategorySerializer()

    class Meta:
        """Serialization options."""

        model = Task
        fields = "__all__"
