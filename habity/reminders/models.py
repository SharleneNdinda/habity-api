import json
from django.db import models
from django_celery_beat.models import CrontabSchedule, PeriodicTask
from cron_converter import Cron
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
    schedule_interval = models.CharField()
    task = models.ForeignKey(
        PeriodicTask,
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.PROTECT,
    )

    def save(self, *args, **kwargs):
        """Save reminder."""
        if self._state.adding:
            try:
                cron = Cron(str(self.schedule_interval)).to_string().split(" ")
            except ValueError:
                err_msg = "Invalid cron format provided!"
                raise ValueError(err_msg)

            schedule, _ = CrontabSchedule.objects.get_or_create(
                minute=cron[0],
                hour=cron[1],
                day_of_week=cron[2],
                day_of_month=cron[3],
                month_of_year=cron[4],
            )

            task = PeriodicTask.objects.create(
                crontab=schedule,
                name=f"{self.task.name}: {self.type}-reminder",
                args=json.dumps([str(self.id)]),
                    task="habity.reminders.tasks.send_task_reminder",
            )
            self.task = task

        super().save(*args, **kwargs)
