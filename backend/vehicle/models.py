from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Manager, Avg


class FriendQuerySet(models.QuerySet):
    def with_average_rate(self):
        return self.annotate(
            average_rate=Avg('rate__rate')
        )


class Vehicle(models.Model):
    make_ID = models.IntegerField()
    make_name = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    objects = FriendQuerySet.as_manager()

    def has_average_rate(self):
        if hasattr(self, 'average_rate'):
            return self.average_rate
        return self.rate_set.aggregate(Avg('rate'))['rate__avg'] or 0


class Rate(models.Model):
    vehicle = models.ManyToManyField(Vehicle)
    rate = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
