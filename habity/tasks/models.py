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


class Task(AbstractBase):
    """Holds task details."""

    category = models.ForeignKey(
        TaskCategory, related_name="tasks", on_delete=models.PROTECT
    )
    user = models.ForeignKey(CustomUser, related_name="tasks", on_delete=models.CASCADE)
    type = models.CharField(choices=TaskType.choices, max_length=50)
    priority = models.CharField()
