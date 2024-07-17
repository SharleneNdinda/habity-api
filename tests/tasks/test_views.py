"""Task view tests."""
from django.urls import reverse
from model_bakery import baker

from habity.tasks.models import Task, TaskCategory
from tests.utils.logged_in_mixin import LoggedInMixin


class TestTaskViews(LoggedInMixin):
    """Test Task views."""

    def test_retrieve_task_successfully(self):
        """Test creating a task successfully."""
        url = reverse("task-list")

        result = self.client.get(url).json()
        assert len(result) == 0

        # create a task
        category = baker.make(
            TaskCategory, name="Music", description="Group all music related tasks"
        )
        baker.make(
            Task, name="Learn Music Fundamentals", category=category, user=self.user, type="SINGLE", priority="HIGH"
        )

        result = self.client.get(url).json()
        assert len(result) == 1

        # with filters
        result = self.client.get(url + "?type=low").json()
        assert len(result) == 1
