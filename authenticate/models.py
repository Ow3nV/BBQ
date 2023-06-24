from django.contrib.auth.models import User
from django.db import models

class UserAddress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address_line_1 = models.CharField(max_length=50, blank=True, null=True)
    address_line_2 = models.CharField(max_length=50, blank=True, null=True)
    town_city = models.CharField(max_length=50, blank=True, null=True)
    county_state = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    postcode = models.CharField(max_length=50, blank=True, null=True)