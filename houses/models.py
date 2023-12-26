from django.db import models

class House(models.Model):
    """ house Model """
    name=models.CharField(max_length=140)
    price_per_night=models.PositiveIntegerField()
    descriotion=models.TextField()
    address=models.CharField(max_length=140)
    pets_allow=models.BooleanField(default=True)