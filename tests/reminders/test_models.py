import pytest
from model_bakery import baker

from habity.reminders.models import Reminder, ReminderType
from habity.tasks.models import Task, TaskCategory
from tests.utils.logged_in_mixin import LoggedInMixin


class TestReminderModel(LoggedInMixin):
    """Test Task models."""

    def test_create_reminder_successfully(self) -> None:
        """Test creating a reminder successfully"""
        category = baker.make(
            TaskCategory, name="Music", description="Group all music related tasks"
        )
        task = baker.make(
            Task, category=category, user=self.user, type="SINGLE", priority="HIGH"
        )
        baker.make(
            Reminder,
            task=task,
            type="Notification",
            schedule_interval="5 4 * * *",
        )

        reminder_qs = Reminder.objects.all()
        assert reminder_qs.count() == 1

        # test with invalid cron string format
        with pytest.raises(ValueError):
            baker.make(
                Reminder,
                task=task,
                type="Notification",
                schedule_interval="5 erfgerg * * *",
            )

        # update existing reminder
        reminder = Reminder.objects.all().first()
        reminder.type = ReminderType.ALARM
        reminder.save()
