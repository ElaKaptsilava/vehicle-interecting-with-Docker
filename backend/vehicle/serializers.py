from django.db import models

from .models import Vehicle, Rate
from rest_framework import serializers


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['make_ID', 'make_name', 'model_name']


class VehicleInitialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['make_name', 'model_name']


class RateSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer(many=True)

    class Meta:
        model = Rate
        fields = ['rate', 'vehicle']
