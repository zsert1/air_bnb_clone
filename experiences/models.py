from django.db import models
from common.models import CommonModel

# Create your models here.


class Experiences(CommonModel):
    name = models.CharField(max_length=250, default="")

    country = models.CharField(
        max_length=50,
        default="korea",
    )
    city = models.CharField(
        max_length=80,
        default="Seoul",
    )
    host = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    price = models.PositiveIntegerField()
    address = models.CharField(
        max_length=250,
    )
    start = models.TimeField()
    end = models.TimeField()
    descriptions = models.TextField()
    perks = models.ManyToManyField("experiences.Perk")
    category = models.ForeignKey(
        "categories.Category",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self) -> str:
        return self.name


class Perk(CommonModel):
    name = models.CharField(max_length=100)
    detail = models.CharField(
        max_length=250,
        blank=True,
        default="",
    )
    explanation = models.TextField(
        blank=True,
        default="",
    )

    def __str__(self) -> str:
        return self.name
