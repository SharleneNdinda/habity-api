from django.db import models

from habity.common.models import AbstractBase
from habity.tasks.models import Task


class ReminderType(models.TextChoices):
    NOTIFICATION = "Notification"
    ALARM = "Alarm"
    NO_REMINDER = "No Reminder"


class DayOfWeek(models.TextChoices):
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"


class Reminder(AbstractBase):
    """Holds reminder details."""

    task = models.ForeignKey(Task, related_name="reminders", on_delete=models.PROTECT)
    type = models.CharField(choices=ReminderType.choices, max_length=100)
    time = models.DateTimeField()


class Schedule(AbstractBase):
    """Holds schedule details."""

    reminder = models.ForeignKey(
        Reminder, related_name="schedules", on_delete=models.PROTECT
    )
    day_of_week = models.CharField(choices=DayOfWeek.choices, max_length=50)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
