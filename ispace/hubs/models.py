from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django.utils.text import slugify

NO_SPACE_ALLOWED = RegexValidator(
    r" ",
    "No spaces allowed",
    inverse_match=True,
    code="invalid_tag",
)

NORMAL_ALPHABET = RegexValidator(
    r"^[a-zA-Z]+$",
    "Lowercase and uppercase alphabet only",
    code="invalid_tag",
)

# Create your models here.
class Hub(models.Model):
    slug = models.SlugField(max_length=32, blank=True)
    owner = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="owned_hub"
    )
    name = models.CharField(
        "Hub's Name",
        max_length=21,
        unique=True,
        validators=[
            NO_SPACE_ALLOWED,
            NORMAL_ALPHABET,
        ],
    )
    description = models.TextField(
        "Hub's Description",
        max_length=500,
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
    )
    member = models.ManyToManyField(
        "users.User",
        related_name="joined_hub",
        blank=True,
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = self.name
        super(Hub, self).save(*args, **kwargs)

    def get_absolute_url(self):
        from django.shortcuts import reverse

        return reverse("hubs:detail", kwargs={"slug": self.slug})
