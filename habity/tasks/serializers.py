from rest_framework.serializers import ModelSerializer

from habity.tasks.models import Task


class TaskSerializer(ModelSerializer):
    """Task Serializer."""

    class Meta:
        """Serialization options."""

        model = Task
        fields = "__all__"
