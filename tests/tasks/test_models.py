from django.contrib.auth import get_user_model
from django.test import TestCase
from model_bakery import baker

from habity.tasks.models import Task, TaskCategory


class TestTaskModels(TestCase):
    """Test Task models."""

    def setUp(self):
        """Create a test user for the logged in session."""
        super().setUp()

        self.user = get_user_model().objects.create_superuser(
            username="jane_doe",
            email="janedoe@gmail.com",
            password="testuser123",
        )

    def test_create_task_successfully(self) -> None:
        """Test creating a tasks successfully"""
        category = baker.make(
            TaskCategory, name="Music", description="Group all music related tasks"
        )
        baker.make(
            Task, category=category, user=self.user, type="SINGLE", priority="HIGH"
        )

        task_qs = Task.objects.all()
        assert task_qs.count() == 1
