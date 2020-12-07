from django.db import models
from django.utils.text import slugify

from ispace.utils.myfunctions import id_generator


# Create your models here.
class Post(models.Model):
    slug = models.SlugField(
        max_length=64,
        unique=True,
        blank=True,
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="has_posted",
    )
    hub = models.ForeignKey(
        "hubs.Hub",
        on_delete=models.CASCADE,
        blank=True,
        related_name="contains_post",
        null=True,
    )
    title = models.CharField(
        "Title",
        max_length=128,
    )
    body = models.TextField(
        "Body",
        max_length=5000,
    )
    date_posted = models.DateTimeField(
        auto_now_add=True,
    )
    last_edited = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(f"{id_generator()} {self.title}")
            self.last_edited = self.date_posted

        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.shortcuts import reverse

        return reverse("posts:detail", kwargs={"slug": self.slug})
