from django.db import models

# Create your models here.
class Gas(models.Model):
    type = models.CharField()
    weight = models.IntegerField()
    price_kg = models.IntegerField()