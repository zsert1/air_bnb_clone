from django.db import models

class House(models.Model):
    """ house Model """
    name=models.CharField(max_length=140)
    price_per_night=models.PositiveIntegerField(verbose_name="Price",help_text="Positive Numbers Only")
    descriotion=models.TextField()
    address=models.CharField(max_length=140)
    pets_allow=models.BooleanField(verbose_name="Pets Allowed", default=True,help_text="Does this house allow pets?")

    def __str__(self):
        return self.name