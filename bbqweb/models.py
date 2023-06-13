from django.db import models


class Barbeque(models.Model):
    name = models.TextField(max_length=100)
    length = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    value = models.IntegerField()
    image = models.ImageField(upload_to='images/', null=True)
    rent_day = models.IntegerField()
    rent_week = models.IntegerField()
    rent_month = models.IntegerField()
    delivery = models.IntegerField()
    pickup = models.IntegerField()
    about = models.TextField(null=True)
