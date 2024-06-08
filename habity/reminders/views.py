from rest_framework.viewsets import ModelViewSet

from habity.reminders.models import Reminder
from habity.reminders.serializers import ReminderSerializer


class ReminderViewSet(ModelViewSet):
    """Reminder ViewSet."""

    serializer_class = ReminderSerializer
    queryset = Reminder.objects.all()
