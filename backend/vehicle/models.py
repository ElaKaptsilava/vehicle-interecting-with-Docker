from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class ModelsManager(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Vehicle(ModelsManager):
    make_ID = models.IntegerField()
    make_name = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)


class Rate(ModelsManager):
    vehicle = models.ManyToManyField(Vehicle)
    rate = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
