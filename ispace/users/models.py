from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

# from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Default user for ispace."""

    bio = models.TextField(
        "User's Bio",
        max_length=500,
        default="This is my Bio",
    )

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
