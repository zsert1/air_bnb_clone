from django.db import models
from common.models import CommonModel


# Create your models here.
class Category(CommonModel):
    class CategotyKindCHoices(models.TextChoices):
        ROOMS = ("rooms", "Rooms")
        EXPERIENCES = ("experiences", "Experiences")

    name = models.CharField(max_length=50)
    kind = models.CharField(
        max_length=15,
        choices=CategotyKindCHoices.choices,
    )

    def __str__(self) -> str:
        return f"{self.kind}:{self.name}"

    class Meta:
        verbose_name_plural = "Categories"
