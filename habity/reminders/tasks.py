"""Reminder tasks."""
from habity.config import celery_app


@celery_app.task()
def send_task_reminder():
    """Send scheduled reminders."""
