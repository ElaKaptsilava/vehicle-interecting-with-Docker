from .models import Vehicle, Rate
from rest_framework.serializers import ModelSerializer, SerializerMethodField


class VehicleSerializer(ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['make_ID', 'make_name', 'model_name', 'has_average_rate']


class RateSerializer(ModelSerializer):
    vehicle = VehicleSerializer(many=True)

    class Meta:
        model = Rate
        fields = ['id', 'rate', 'vehicle']
