from django.db import models


class Barbeque(models.Model):
    name = models.TextField(max_length=100)
    length = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    weight = models.CharField(max_length=10)
    burners = models.IntegerField()
    side_burners = models.IntegerField()
    cook_width = models.IntegerField()
    cook_length = models.IntegerField()
    gas = models.CharField(max_length=15)
    value = models.IntegerField()
    image = models.ImageField(upload_to='images/', null=True)
    rent = models.IntegerField()
    delivery = models.IntegerField()
    pickup = models.IntegerField()
    about = models.TextField(null=True)


class Images(models.Model):
    barbeque = models.ForeignKey(Barbeque, on_delete=models.CASCADE)
    image1 = models.ImageField(null=True, blank=True, upload_to='images/')
    image2 = models.ImageField(null=True, blank=True, upload_to='images/')
    image3 = models.ImageField(null=True, blank=True, upload_to='images/')
    image4 = models.ImageField(null=True, blank=True, upload_to='images/')
