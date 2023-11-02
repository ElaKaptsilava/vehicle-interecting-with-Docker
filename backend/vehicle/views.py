from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from .models import Vehicle, Rate
from .serializers import VehicleSerializer, RateSerializer

class RateViewSet(ModelViewSet):
    serializer_class = RateSerializer
    queryset = Rate.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['rate']


class VehicleViewSet(ModelViewSet):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['model_name', 'make_name']
