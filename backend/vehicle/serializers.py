from django.db import models

from .models import Vehicle, Rate
from rest_framework import serializers


class VehicleSerializer(serializers.ModelSerializer):
    average_rate = serializers.SerializerMethodField()

    class Meta:
        model = Vehicle
        fields = ['pk', 'make_ID', 'make_name', 'model_name', 'average_rate']

    def get_average_rate(self, obj):
        return obj.rate_set.aggregate(models.Avg('rate'))['rate__avg'] or 0


class RateSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer(many=True)

    class Meta:
        model = Rate
        fields = ['id', 'rate', 'vehicle']
