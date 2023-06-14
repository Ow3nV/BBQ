from django.contrib.auth.models import User
from django.db import models

from bbqweb.models import Barbeque


# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    barbeque = models.ForeignKey(Barbeque, on_delete=models.CASCADE)
    date_from = models.DateField()
    date_to = models.DateField()
    sub_total = models.IntegerField()
    address_line_1 = models.CharField()
    address_line_2 = models.CharField()
    town_city = models.CharField()
    county = models.CharField()
    postcode = models.CharField()
    delivery = models.BooleanField()
    completed = models.BooleanField()

