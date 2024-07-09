from django.contrib.auth import get_user_model
from django.test import TestCase
import pytest


class TestUserModels(TestCase):
    """Test User models."""

    def test_create_user_with_missing_parameters(self):
        """Create user with missing email."""

        with pytest.raises(ValueError) as exc_info:
            get_user_model().objects.create_user(
                email=None,
                username="jane_doe",
                password="testuser123",
            )

        assert str(exc_info.value) == "The Email field must be set"

        with pytest.raises(ValueError) as exc_info:
            get_user_model().objects.create_superuser(
                email="test123@gmail.com",
                username="jane_doe",
                password="testuser123",
                is_staff=False,
            )

        assert str(exc_info.value) == "Superuser must have is_staff=True."

        with pytest.raises(ValueError) as exc_info:
            get_user_model().objects.create_superuser(
                email="test123@gmail.com",
                username="jane_doe",
                password="testuser123",
                is_superuser=False,
            )

        assert str(exc_info.value) == "Superuser must have is_superuser=True."
