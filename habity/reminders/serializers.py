from rest_framework.serializers import ModelSerializer

from habity.reminders.models import Reminder


class ReminderSerializer(ModelSerializer):
    """Reminder Serializer."""

    class Meta:
        """Serialization options."""

        model = Reminder
        fields = "__all__"
