from model_bakery import baker

from habity.tasks.models import Task, TaskCategory
from tests.utils.logged_in_mixin import LoggedInMixin


class TestTaskModel(LoggedInMixin):
    """Test Task models."""

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
