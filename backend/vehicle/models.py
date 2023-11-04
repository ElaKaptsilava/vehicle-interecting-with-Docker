from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Vehicle(models.Model):
    make_ID = models.IntegerField()
    make_name = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)


class Rate(models.Model):
    vehicle = models.ManyToManyField(Vehicle)
    rate = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
