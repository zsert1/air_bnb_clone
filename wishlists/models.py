from django.db import models
from common.models import CommonModel


# Create your models here.
class WishList(CommonModel):
    name = models.CharField(max_length=150)
    roooms = models.ManyToManyField(
        "rooms.Room",
        related_name="wishlists",
    )
    experiences = models.ManyToManyField(
        "experiences.Experiences",
        related_name="wishlists",
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="wishlists",
    )

    def __str__(self) -> str:
        return self.name
