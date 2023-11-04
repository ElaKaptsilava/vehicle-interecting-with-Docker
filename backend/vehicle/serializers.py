from django.db import models

from .models import Vehicle, Rate
from rest_framework import serializers


class VehicleSerializer(serializers.ModelSerializer):
    has_agr_rate = serializers.SerializerMethodField()
    is_max = serializers.SerializerMethodField()

    class Meta:
        model = Vehicle
        fields = ['make_ID', 'make_name', 'model_name', 'has_agr_rate', 'is_max']

    def get_has_agr_rate(self, obj):
        if hasattr(obj, 'agr_rate'):
            return obj.agr_rate
        return obj.rate_set.aggregate(models.Avg('rate'))['rate__avg'] or 0

    def get_is_max(self, obj):
        max_rate = self.context['popular']
        return obj.rate == max_rate


class RateSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer(many=True)

    class Meta:
        model = Rate
        fields = ['id', 'rate', 'vehicle']
