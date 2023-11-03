from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Manager(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Vehicle(Manager):
    make_ID = models.IntegerField()
    make_name = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)

    @property
    def average_rate(self):
        try:
            vehicle = Vehicle.objects.get(pk=self.pk)
            vehicle_rates = [rate_instance.rate for rate_instance in vehicle.rate_set.all()]
            return sum(vehicle_rates)/len(vehicle_rates)
        except ZeroDivisionError:
            return 0


class Rate(Manager):
    vehicle = models.ManyToManyField(Vehicle)
    rate = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
