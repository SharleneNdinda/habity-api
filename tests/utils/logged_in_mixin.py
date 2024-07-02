from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase


class LoggedInMixin(APITestCase):
    """Logged in testcase for running authenticated tests."""

    def setUp(self):
        """Setup testing environmet."""
        self.user = get_user_model().objects.create_superuser(
            username="jane_doe",
            email="janedoe@gmail.com",
            password="testuser123",
        )
        self.client.login(username="jane_doe", password="testuser123")
