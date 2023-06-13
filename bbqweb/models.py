from django.db import models


class Barbeque(models.Model):
    name = models.CharField(max_length=100)
    dimensions = models.CharField(max_length=50)
    value = models.IntegerField()
    image = models.ImageField(upload_to='images/', null=True)
    rent = models.IntegerField()
    delivery = models.IntegerField()
