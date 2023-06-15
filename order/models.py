from django.contrib.auth.models import User
from django.db import models

from bbqweb.models import Barbeque


# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    barbeque = models.ForeignKey(Barbeque, on_delete=models.CASCADE)
    sub_total = models.IntegerField()
    date_from = models.DateField()
    date_to = models.DateField()
    address_line_1 = models.CharField(max_length=50)
    address_line_2 = models.CharField(max_length=50, blank=True, null=True)
    town_city = models.CharField(max_length=50)
    county = models.CharField(max_length=50)
    postcode = models.CharField(max_length=50)
    delivery = models.BooleanField()
    pick_up = models.BooleanField()
    paid = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

