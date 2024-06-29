from django.contrib.auth import get_user_model
from django.test import TestCase
from model_bakery import baker

from habity.tasks.models import Task, TaskCategory


class TestTaskModels(TestCase):
    """Test Task models."""

    def test_create_task_successfully(self) -> None:
        """Test creating a tasks successfully"""
        user = get_user_model().objects.create_user(
            username="jane_doe",
            email="janedoe@gmail.com",
            password="testuser123",
        )
        category = baker.make(
            TaskCategory, name="Music", description="Group all music related tasks"
        )
        baker.make(Task, category=category, user=user, type="SINGLE", priority="HIGH")

        task_qs = Task.objects.all()
        assert task_qs.count() == 1
