from django.db import models

from habity.common.models import AbstractBase
from habity.users.models import CustomUser


class TaskCategory(AbstractBase):
    """Holds categories a task can belong to."""

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)


class TaskType(models.TextChoices):
    SINGLE = "Single"
    RECURRING = "Recurring"
    HABIT = "Habit"


class Priority(models.TextChoices):
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"


class Task(AbstractBase):
    """Holds task details."""

    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(
        TaskCategory, related_name="tasks", on_delete=models.PROTECT
    )
    user = models.ForeignKey(CustomUser, related_name="tasks", on_delete=models.CASCADE)
    type = models.CharField(choices=TaskType.choices, max_length=50)
    priority = models.CharField(choices=Priority.choices, max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
