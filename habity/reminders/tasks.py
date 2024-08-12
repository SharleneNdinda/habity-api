"""Reminder tasks."""
from habity.config import celery_app


@celery_app.task()
def send_scheduled_task_reminder():
    """Send scheduled task reminders."""
    pass
