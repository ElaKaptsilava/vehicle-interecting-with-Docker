import requests

from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction, models
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Vehicle, Rate
from .serializers import VehicleSerializer, RateSerializer, VehicleInitialSerializer


class RateViewSet(ModelViewSet):
    serializer_class = RateSerializer
    queryset = Rate.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['rate', 'vehicle']


class VehicleViewSet(ModelViewSet):
    serializer_class = VehicleInitialSerializer
    queryset = Vehicle.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['model_name', 'make_name']

    def create(self, request, *args, **kwargs):
        serializer_initial_vehicle = self.serializer_class(data=request.data)
        serializer_initial_vehicle.is_valid(raise_exception=True)
        model_name = serializer_initial_vehicle.validated_data.get('model_name', None)
        make_name = serializer_initial_vehicle.validated_data.get('make_name', None)
        vehicle_data = self.create_from_link(model_name_params=model_name, make_name_params=make_name)
        serializer_vehicle = VehicleSerializer(data=vehicle_data)
        serializer_vehicle.is_valid(raise_exception=True)
        serializer_vehicle.save()
        return Response(serializer_vehicle.data, status=status.HTTP_201_CREATED)

    @staticmethod
    def create_from_link(model_name_params, make_name_params):
        url = r'https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformakeyear/make/{0}/vehicleType/car?format=json'.format(
            make_name_params)
        get_link = requests.get(url)
        vpic_data = get_link.json()
        for item in vpic_data['Results']:
            if model_name_params == item['Model_Name']:
                data = {
                    'make_ID': item['Make_ID'], 'make_name': item['Make_Name'], 'model_name': item['Model_Name']
                }
                return data
        raise APIException(
            f'Vehicle with model name:{model_name_params}, make name:{make_name_params} dose not exist.'
            f'into link {url}'
        )

    @action(methods=['GET'], detail=True, url_path='rate', url_name='rate')
    def get_rate(self, request, pk=None):
        vehicle = Vehicle.objects.get(pk=pk)
        vehicle_rates = vehicle.rate_set.all()
        rate_serializer = RateSerializer(instance=vehicle_rates, many=True)
        return Response(rate_serializer.data)

    @action(methods=['GET'], detail=False, url_path='popular-by-bayesian', url_name='popular-by-bayesian')
    def get_popular_vehicle_by_bayesian(self, request):
        prior_mean = 4.0
        prior_weight = 10
        get_popular_by_bayesian = self.queryset.annotate(
            bayesian_average=(
                    ((models.Count('rate') * models.Avg('rate')) + (prior_weight * prior_mean)) /
                    (models.Count('rate') + prior_weight)
            )
        ).order_by('bayesian_average').first()
        vehicle_serializer = VehicleSerializer(instance=get_popular_by_bayesian)
        return Response(vehicle_serializer.data)

    @action(methods=['GET'], detail=False, url_path='popular', url_name='popular')
    def get_popular_vehicle(self, request):
        get_popular = self.queryset.annotate(count=models.Count('rate')).order_by('-count').first()
        vehicle_serializer = VehicleSerializer(instance=get_popular)
        return Response(vehicle_serializer.data)
