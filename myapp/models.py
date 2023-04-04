from django.db import models

# Create your models here.
class register(models.Model):
    uname=models.CharField(max_length=100)
    email=models.CharField(max_length=150)
    password = models.CharField(max_length=63)


class additems(models.Model):
    itemname = models.CharField(max_length=50)
    amount = models.IntegerField(null=True, blank=True, default=None)