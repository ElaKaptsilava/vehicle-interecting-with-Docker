from .models import Vehicle, Rate
from rest_framework.serializers import ModelSerializer


class VehicleSerializer(ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'


class RateSerializer(ModelSerializer):
    class Meta:
        model = Rate
        fields = '__all__'
