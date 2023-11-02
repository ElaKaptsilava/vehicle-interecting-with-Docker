from django.db import models


class Manager(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Vehicle(Manager):
    make_ID = models.IntegerField()
    make_name = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)


class Rate(Manager):
    vehicle = models.ManyToManyField(Vehicle)
    rate = models.IntegerField(default=0)
