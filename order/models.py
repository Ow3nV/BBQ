from django.db import models

from bbqweb.models import Barbeque


# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(barbeque = models.ForeignKey(Barbeque, on_delete=models.CASCADE))