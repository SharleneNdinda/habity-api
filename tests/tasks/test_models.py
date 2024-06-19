"""Task model tests."""
from model_bakery import baker

from habity.tasks.models import Task, TaskCategory
from tests.common.common_views import LoggedInTestCase


class TestTaskModel(LoggedInTestCase):
    """Test task related models."""


def test_create_task_successfully(self):
    """Test creating a task successfully."""
    category = baker.make(
        TaskCategory, name="Music", description="Group all music related tasks"
    )
    task = baker.make(Task, category=category, user="", type="SINGLE", priority="HIGH")
